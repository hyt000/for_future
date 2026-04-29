# Definition for a binary tree node.
from typing import Optional

"""
由于题目要求next()和hasnext的时间复杂度是O(1)，
不难想到在init环节就将中序遍历的结果保存起来
1.  中序遍历如何实现
    对于某个确定的节点node
    很自然想到先把node左边的所有节点处理完，
    在处理中间node节点，在处理node右边的所有节点,于是可以递归地实现
    递归先要想好返回值和停止条件
    第一，想清楚函数定义
    把以 node 为根的这棵树，按照中序遍历加入 res
    这里它只是负责“把结果加入 res”，不需要返回一个新结果，所以返回值可以是None
    第二，想停止条件
    node 是空节点的时候
    第三，想单层逻辑：当前这一层要做什么？怎么把任务交给下一层？

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.res = self.Inorder_Traversal(root)
        self.length = len(self.res)
        self.temp_locate = 0

    def next(self) -> int:
        result = self.res[self.temp_locate].val
        self.temp_locate +=1
        return result

    def hasNext(self) -> bool:
        if self.temp_locate>=self.length:
            return False
        return True

    def Inorder_Traversal(self,root):
        res = []
        def inorder_traversal(node):
            if not node:
                return  None
            inorder_traversal(node.left)
            res.append(node)
            inorder_traversal(node.right)
        inorder_traversal(root)
        return res


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()