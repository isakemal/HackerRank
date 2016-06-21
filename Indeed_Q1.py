#!/usr/bin/env python
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None

def _insert_node_into_binarysearchtree(node, data):
    if node == None:
        node = BSTreeNode(data)
    else:
        if (data <= node.value):
            node.left = _insert_node_into_binarysearchtree(node.left, data);
        else:
            node.right = _insert_node_into_binarysearchtree(node.right, data);
    return node


"""
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
"""


def isPresent(root, val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    # This is a binary search tree
    if root is None:
        return 0

    if root.value == val:
        return 1
    # Check to see which direction to go
    # exit condition is
    # Existence of value
    # No more nodes to check
    if val < root.value:
        return isPresent(root.left, val)

    return isPresent(root.right, val)


if __name__ == '__main__':

    _a = None
    _a_size = 5
    _a_i=0
    inputs = [1, 2, 3, 4]
    for i in inputs:
        _a = _insert_node_into_binarysearchtree(_a, i)

    _b = 5

    _result = isPresent (_a , _b );
    print _result