from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            y = self.root
            while True:
                if data == y.key:
                    print("Can't insert %d. Already exists" % data)
                    return
                if data < y.key:
                    if y.left is not None:
                        y = y.left
                    else:
                        y.left = Node(data)
                        break;
                elif data > y.key:
                    if y.right is not None:
                        y = y.right
                    else:
                        y.right = Node(data)
                        break

    def parent(self, data):
        """
        for ease of use will
        return root if data is root
        TODO: think about this sometime
        it's not nice
        """

        if self.root.key == data:
            return self.root
        y = self.root
        while True:
            if y.left is not None:
                if y.left.key is data:
                    return y
            if y.right is not None:
                if y.right.key is data:
                    return y
            if data < y.key:
                if y.left is None:
                    break
                y = y.left
            elif data > y.key:
                if y.right is None:
                    break
                y = y.right
        return None

    def find(self, data):
        y = self.root
        while True:
            if y.key == data:
                return y
            if data < y.key:
                if y.left is not None:
                    y = y.left
                else:
                    return
            else:
                if y.right is not None:
                    y = y.right
                else:
                    return

    def min_in_left_sub(self, data):
        """
        :return: the minimum node value in the left subtree
        """
        y = self.find(data).left
        while y.right is not None:
            y = y.right
        return y

    def del_node_helper(self, data):
        """
        helps DelNode
        by not rewriting this whole stuff again
        for various cases
        """

        p = self.parent(data)
        if p.left.key == data:
            del data
            p.left = None
        else:
            del data
            p.right = None

    def del_node(self, data):
        print("Deleting", data)
        x = self.find(data)
        if x is None:
            return
        # case 1: has no children
        if x.left is None and x.right is None:
            self.del_node_helper(x)
            return
        # case 2: has at least left child
        if x.left is not None:
            min_left = self.min_in_left_sub(x.key)
            self.del_node_helper(min_left.key)
            x.key = min_left.key
            return
        # case 3: only right child
        if x.right is not None:
            p = self.parent(x.key)
            p.right = x.right
            del x
            return

    def in_order_transversal(self, x):
        """
        recursive transversal
        TODO: sometime, implement the non-recursive one
        """
        print(x.key)
        if x.left is not None:
            self.in_order_transversal(x.left)
        if x.right is not None:
            self.in_order_transversal(x.right)
