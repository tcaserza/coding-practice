#
# PROBLEM: Implement a binary search tree
#


class Node:
    value = None
    left = None
    right = None
    def __init__(self,val):
        self.value = val


def insert(value,top):
    if value > top.value:
        if top.right is not None:
            insert(value,top.right)
        else:
            top.right = Node(value)
    if value < top.value:
        if top.left is not None:
            insert(value,top.left)
        else:
            top.left = Node(value)


def delete(value,top):
    print value,top.value
    if value == top.value:
        top.value = find_min_value(top.right)
        delete(top.value,top.right)
    if value < top.value:
        delete(value,top.left)
    if value > top.value:
        delete(value,top.right)


def find_min_value(top):
    if top.left is not None:
        return find_min_value(top.left)
    else:
        return top.value

def printBST(top):
    if top.left is not None:
        printBST(top.left)
    print top.value
    if top.right is not None:
        printBST(top.right)


top = Node(5)
insert(6,top)
insert(1,top)
insert(3,top)
insert(2,top)
insert(4,top)
insert(9,top)
insert(7,top)
delete(3,top)
print printBST(top)