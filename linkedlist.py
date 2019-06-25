#
# PROBLEM: Implement a linked list
#


class Node:
    def __init__(self,value):
        self.value = value
        self.nextnode = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.nextnode = self.head
        self.head = new_node

    def delete(self,value):
        temp = self.head
        if temp is not None and temp.value == value:
            self.head = temp.nextnode
            temp = None
            return
        while temp.nextnode is not None and temp.nextnode.nextnode is not None:
            if temp.nextnode.value == value:
                temp.nextnode = temp.nextnode.nextnode
            temp = temp.nextnode
        temp = None

    def print_list(self):
        temp = self.head
        while temp.nextnode is not None:
            print temp.value
            temp = temp.nextnode


linked_list = LinkedList()
linked_list.push(9)
linked_list.push(5)
linked_list.push(7)
linked_list.push(3)
linked_list.push(4)
linked_list.delete(3)
linked_list.delete(9)
linked_list.delete(4)
print linked_list.print_list()



