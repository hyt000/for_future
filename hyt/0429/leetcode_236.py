# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
leetcode236
思路是这样的：
    1. 我想把二叉树的每一个选择记录成0和1，0代表选左，1代表右
    2. 层序遍历得到两个的traj,记录为0和1的轨迹
    3. 记录根节点，两个轨迹第一个必相同。
    4. 假设轨迹长度分别为len_a和len_b，len_a<len_b
    5. 如果b的前len_a个和a完全一样，则祖先是a
    6. 对比a和b前面有几个相同。根据这个找到公共祖先
从当前的 node 出发，去寻找 target 节点。在这个探索过程中，把沿途踩过的节点记录在 path 里。
如果这是一条死路，就把最后踩的那个节点从 path 里擦除掉。
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(node,target,path):
            #空节点
            if not root:
                return  False
            #假设这个是正确路径
            path.append(node)
            #找到了就返回这个路径
            if node == target:
                return True
            #不然从子节点找
            if get_path(node.left,target,path) or get_path(node.left,target,path):
                return True
            #子节点都没找到,把这个节点移除
            path.pop()
            return False
        path_p = []
        path_q = []
        # 1. 拿到两条真实的节点轨迹
        get_path(root, p, path_p)
        get_path(root, q, path_q)
        # 2. 对比轨迹
        res = []
        for u,v in zip(path_p,path_q):
            if u==v:
               res = u
            else:
                break