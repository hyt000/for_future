# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#
# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层（从第 0 层开始），则该层包含 1~ 2h 个节点。
from typing import Optional
"""
解题：
你站在根节点看左右子树，一定会出现一种情况：
左子树是满的
或者：
右子树是满的
也就是说，每次至少有一边可以直接用公式算，不需要递归数。
同时注意到，这个题由是可以不断拆成一个小树计算有多少个节点，于是用递归，
那么，
1.  递归的终止条件是什么？
    也就是这个函数处理到什么情况，答案已经简单到不需要继续拆了？
    不难发现是root is None
    此时return 0
2.  那怎么判断哪边是满的？如果考虑左边第一个和root.right然后一直去左边
    一共有两种情况
    left_h==right__h,说明左边满
    和
    left>right_h说明右边满
3.  那怎么计算高度h？
    当最左边的节点存在，这个高度就加一
4.  左子树高度是 left_h，节点数是：
    2 ** left_h - 1
    再加上根节点，就是：
    2 ** left_h
    然后再加上右边的总节点数就可以。所以代码是：
    return (1 << left_h) + self.countNodes(root.right)
    不难想到第二种是return (1 << right_h) + self.countNodes(root.left)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def count_h(node):
            h = 1
            if not node:
                return 0
            while node.left:
                h+=1
                node = node.left
            return h
        left_h = count_h(root.left)
        right_h = count_h(root.right)
        if left_h==right_h:
            return (1<<left_h)+self.countNodes(root.right)
        else:
            return (1<<right_h) + self.countNodes(root.left)





















