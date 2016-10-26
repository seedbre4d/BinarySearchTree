from binarysearchtree import BinarySearchTree

tree = BinarySearchTree()
array = [8, 3, 3, 1, 0, 2, 6, 4, 7, 13, 19, 20, 21]

for i in array:
    tree.add_node(i)
tree.in_order_traversal(tree.root)
tree.del_node_helper(13)
tree.in_order_traversal(tree.root)
