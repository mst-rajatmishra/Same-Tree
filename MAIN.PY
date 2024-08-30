class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both nodes are None, the trees are the same
        if not p and not q:
            return True
        
        # If one node is None and the other is not, the trees are different
        if not p or not q:
            return False
        
        # If both nodes are not None, check their value and their subtrees
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Example usage:
solution = Solution()

# Construct example trees
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(solution.isSameTree(p1, q1))  # Output: True

p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print(solution.isSameTree(p2, q2))  # Output: False

p3 = TreeNode(1, TreeNode(2, TreeNode(1)))
q3 = TreeNode(1, TreeNode(1, None, TreeNode(2)))
print(solution.isSameTree(p3, q3))  # Output: False
