# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None: return

        first_up_level = root

        while first_up_level:

            next_up_level_node = first_up_level
            first_up_level = None

            while next_up_level_node:
                # if it is the first node in up level
                if not first_up_level:
                    if next_up_level_node.left and next_up_level_node.right:
                        first_up_level = next_up_level_node.left
                        next_up_level_node.left.next = next_up_level_node.right
                        prev = next_up_level_node.right
                    elif next_up_level_node.left and not next_up_level_node.right:
                        first_up_level = next_up_level_node.left
                        prev = next_up_level_node.left
                    elif not next_up_level_node.left and next_up_level_node.right:
                        first_up_level = next_up_level_node.right
                        prev = next_up_level_node.right

                else:
                    if next_up_level_node.left and next_up_level_node.right:
                        prev.next = next_up_level_node.left
                        next_up_level_node.left.next = next_up_level_node.right
                        prev = next_up_level_node.right
                    elif next_up_level_node.left and not next_up_level_node.right:
                        prev.next = next_up_level_node.left
                        prev = next_up_level_node.left
                    elif not next_up_level_node.left and next_up_level_node.right:
                        prev.next = next_up_level_node.right
                        prev = next_up_level_node.right

                next_up_level_node = next_up_level_node.next
