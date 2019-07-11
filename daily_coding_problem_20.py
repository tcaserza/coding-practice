# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
#
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
#
# In this example, assume nodes with the same value are the exact same node objects.
#
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


class LinkedList:
    def __init__(self, value, nextnode=None):
        self.value = value
        self.nextnode = nextnode



def find_intersection(node1,node2):
    list1 = set()
    while node1.nextnode is not None:
        list1.add(node1.value)
        node1 = node1.nextnode
    while node2.nextnode is not None:
        if node2.value in list1:
            return node2.value
        node2 = node2.nextnode
    return None


list1 = LinkedList(3,LinkedList(7,LinkedList(8,LinkedList(10))))
list2 = LinkedList(99,LinkedList(1,LinkedList(8,LinkedList(10))))
print find_intersection(list1,list2)