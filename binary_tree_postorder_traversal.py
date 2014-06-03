# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None: return []

        stack = [root]
        prev = None
        result = []

        while len(stack) > 0:
            curr = stack[-1]
            if not prev or prev.left == curr or prev.right == curr:
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
                else:
                    result.append(curr.val)
                    stack.pop()
            elif curr.left == prev:
                if curr.right:
                    stack.append(curr.right)
                else:
                    result.append(curr.val)
                    stack.pop()
            elif curr.right == prev:
                result.append(curr.val)
                stack.pop()

            prev = curr

        return result



if __name__ == '__main__':
    node = TreeNode(3)
    node.left = TreeNode(1)
    node.right = TreeNode(2)

    print Solution().postorderTraversal(node)
