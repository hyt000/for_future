# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和
# Definition for a binary tree node.
"""
既然答案一定是某个“最高点”所在的倒 V 型路径，那我们就遍历树的每一个节点，假设它就是那个“最高点”，算一下它的倒 V 型总和，然后挑出最大的那个！
从上到下递归的来实现，先实现根节点的倒V最大值，由是需要左右节点的最大值，依次类推，直到叶子节点。然后一路一路返回当前支路的最大贡献，不断地更新
全局变量max_sum
"""
"""
1. 我要向子节点索取什么？（过滤负资产）
物理意义： 我需要左右子树提供一条连续路径。但如果他们给的是负数（只会拖累我），我直接当他们不存在（取 0）。
2. 我的对内任务是什么？（拼凑全局最大 V 型）
物理意义： 假设我就是这条路径的最高点，我把我能拿到的所有正收益（左 + 我自身 + 右）全加起来，
去全局记分板上碰碰运气，看能不能打破历史记录。
3. 我的对外任务是什么？（向上级汇报单边最大值）
物理意义： 我的父节点在等我（必须包含父节点），所以二叉树不能分叉，
我只能把我自己（node.val），加上左右两边中较大的一条边，捆绑成一条不分叉的线头，递给父节点。
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]):
        def calculate_current_max(root):
            if not root:
                return 0
            cur_val = root.val
            left_val = max(calculate_current_max(root.left),0)
            right_val = max(calculate_current_max(root.right),0 )
            temp_val = cur_val + left_val +right_val
            self.max_sum = temp_val if temp_val>self.max_sum else self.max_sum
            #这个return只是为了上传给父节点，让他知道这条支路的最大贡献
            return cur_val + max(left_val,right_val)


        calculate_current_max(root)

        return self.max_sum

