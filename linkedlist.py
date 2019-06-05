#
# PROBLEM: Implement a linked list
#


class Node:
    left = None
    right = None
    value = None
    def __init__(self,value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def insert(value,node):
    if value > node.value:
        if node.right is None or value < node.right.value:
            node.right = Node(value, node, node.right)
            if node.right.right is not None:
                node.right.right.left = node.right
        else:
            insert(value,node.right)

    if value < node.value:
        if node.left is None or value > node.left.value:
            node.left = Node(value, node.left, node)
            if node.left.left is not None:
                node.left.left.right = node.left
        else:
            insert(value,node.left)


def print_list(node):
    while node.left is not None:
        node = node.left
    while node.right is not None:
        print "%s,%s,%s" % (node.value, output(node.left), output(node.right))
        node = node.right
    print "%s,%s,%s" % (node.value, output(node.left), output(node.right))

def output(node):
    if node is None:
        return 0
    else:
        return node.value

main_node = Node(5)
insert(1,main_node)
insert(9,main_node)
insert(3,main_node)
insert(7,main_node)
insert(2,main_node)
print print_list(main_node)



