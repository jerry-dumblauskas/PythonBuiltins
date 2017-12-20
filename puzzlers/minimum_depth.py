class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def find_depth(node):
    if not node.left and not node.right:
        return 1

    if not node.right:
        return 1 + find_depth(node.left)

    if not node.left:
        return 1 + find_depth(node.right)

    return 1 + min(find_depth(node.left), find_depth(node.right))


if __name__ == '__main__':
    head_node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)

    node9.left = node12
    node9.right = node13

    node8.left = node10
    node8.right = node11

    node6.left = node9

    node5.right = node8

    node4.left = node7

    node2.right = node4

    node3.left = node5
    node3.right = node6

    head_node.left = node2
    head_node.right = node3

    res = find_depth(head_node)

    print(res)
