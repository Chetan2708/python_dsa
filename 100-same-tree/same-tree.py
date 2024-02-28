# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution :
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse (root,l):
            if root == None:
                l.append(None)
                return  
            l.append(root.val)
            left = traverse(root.left , l  )
            right = traverse(root.right , l)
        

        l1 =[]
        l2 = []
        traverse(p , l1)
        traverse(q ,l2)
        if l1==l2:
            return True
        else:
            return False
