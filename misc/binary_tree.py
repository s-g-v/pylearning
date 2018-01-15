#!/usr/bin/env python3
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = Node(value)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left:
                self._insert(value, cur_node.left)
            else:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
        elif value > cur_node.value:
            if cur_node.right:
                self._insert(value, cur_node.right)
            else:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
        else:
            print("Value already in the tree")

    def print(self):
        if self.root:
            self._print(self.root, 10)
        else:
            print("ERROR. Tree has no root")

    # def _print(self, cur_node, shift):
    #     if cur_node:
    #         print(shift * " " + str(cur_node.value))
    #         self._print(cur_node.left, shift - 1)
    #         self._print(cur_node.right, shift + 1)

    def _print(self, cur_node, shift):
        if not cur_node:
            return
        if not cur_node.parent:
            print((shift + 1) * " " + str(cur_node.value))
        to_print = shift * " "
        if cur_node.left:
            to_print += str(cur_node.left.value)
        if cur_node.right:
            to_print += " " + str(cur_node.right.value)
        if cur_node.left or cur_node.right:
            print(to_print)
        self._print(cur_node.left, shift - 1)
        self._print(cur_node.right, shift + 1)

    def height(self):
        return self._height(self.root, 0) if self.root else 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def is_present(self, value):
        return True if self.find(value) else False

    def find(self, value):
        return self._find(value, self.root) if self.root else None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right:
            return self._find(value, cur_node.right)
        else:
            return None

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):

        def min_value_node(n):
            cur = n
            while cur.left:
                cur = cur.left
            return cur

        def num_children(n):
            num = 0
            if n.left:
                num += 1
            if n.right:
                num += 1
            return num

        def set_node_to(n):
            if node_parent.left == node:
                node_parent.left = n
            else:
                node_parent.right = n

        node_parent = node.parent
        node_children = num_children(node)

        if node_children == 0:
            set_node_to(None)

        if node_children == 1:
            child = node.left if node.left else node.right
            set_node_to(child)
            child.parent = node_parent

        if node_children == 2:
            successor = min_value_node(node.right)
            node.value = successor.value
            self.delete_node(successor)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in [6, 4, 5, 3, 7, 10, 9, 11]:
        tree.insert(i)
    tree.print()
    print('Height: %s' % tree.height())
    print('Delete value 7')
    tree.delete_value(7)
    tree.print()
