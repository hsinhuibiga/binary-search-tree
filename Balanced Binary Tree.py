#Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def TreeDepth(root):
            left_depth,right_depth=0,0
            if root.left:
                left_depth=TreeDepth(root.left)
            if root.right:
                right_depth=TreeDepth(root.right)
            if left_depth==-1 or right_depth==-1 or abs(left_depth-right_depth)>1:
                return -1
            return max(left_depth,right_depth)+1
        depth=0
        if root:
            depth=TreeDepth(root);
        return depth!=-1