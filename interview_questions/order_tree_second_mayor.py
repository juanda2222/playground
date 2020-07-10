

# Property always holds: root.val = min(root.left.val, root.right.val)


        
import numpy as np


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self, root):
        
        # Recursive
        tree_list = []
        def convert_to_global_array(node):
            
            # if the node is none append none
            if node is None:
                return tree_list.append(None)

            # append the value
            tree_list.append(node.val)

            # append the next two nodes:
            convert_to_global_array(node.left)
            convert_to_global_array(node.right)

        convert_to_global_array(root)
        return tree_list

    def deserialize(self, data):
        
        # Recursive
        def dfs(it):
            val = next(it) 
            if val is None:
                return None
            cur = TreeNode(val)
            cur.left, cur.right = dfs(it), dfs(it)
            return cur
        return dfs(iter(data))

    def beauty_print(self, serialized_root:list):

        
        jump_index = 0

        for i, node in enumerate(serialized_root):
            if i <= jump_index:
                print(node, end =" ")

            # time to jump line:
            else:
                print(node, end =" ")
        
        
        def do(root, n_space=4):
            
            # check if none print nothing
            if root is None:
                return
            
            # check each child and if child print with lines:
            print(n_space*" ", root.val)
            print( int(n_space/2) * " ", "/", "  ", "" )
            print(root.left)
            
            
        

class Solution:
    def serialize(self, root: TreeNode) -> list:
        
        # Recursive
        tree_list = []
        def convert_to_global_array(node):
            
            # if the node is none append none
            if node is None:
                return tree_list.append(None)

            # append the value
            tree_list.append(node.val)

            # append the next two nodes:
            convert_to_global_array(node.left)
            convert_to_global_array(node.right)

        convert_to_global_array(root)
        return tree_list

    def findSecondMinimumValue(self, root: TreeNode) -> int:
                
        #check if the root has childs:
        if root.left is None or root.right is None:
            print("None detected")
            return -1
        # check if the axiom holds
        if root.val is not min(root.left.val, root.right.val) or \
            (root.val is root.left.val and root.val is root.right.val):
            return -1

        serialized = self.serialize(root)
        minimum_second = np.inf

        # loop through the array and find the second smallest:
        for node_val in serialized:
            if node_val is not None:
                if node_val > root.val and node_val < minimum_second:
                    minimum_second = node_val

        return minimum_second



binary_tree = TreeNode(
    2, TreeNode(2), TreeNode(
        5, TreeNode(5), TreeNode(7)
    )
)
binary_tree2 = TreeNode(2)

#binary_tree3 = TreeNode(
#    2, TreeNode(2), TreeNode(2)
#)

#binary_tree4 = TreeNode().deserialize([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])


sol = Solution()
ret = sol.findSecondMinimumValue(binary_tree)
print("Return:", ret)