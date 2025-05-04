class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Append new data to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Print all elements of the linked list
    def print_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    # Reverse the linked list by changing node pointers
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Insert a node into a sorted linked list
    def sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or new_node.data <= sorted_head.data:
            new_node.next = sorted_head
            sorted_head = new_node
        else:
            current = sorted_head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_head

    # Sort linked list using insertion sort
    def insertion_sort(self):
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.sorted_insert(sorted_head, current)
            current = next_node
        self.head = sorted_head

# Merge two sorted linked lists into one sorted linked list
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    result = LinkedList()
    result.head = dummy.next
    return result

# Example usage:

# Create a list and append elements
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)

print("Original list:")
ll.print_list()

# Reverse the list
ll.reverse()
print("Reversed list:")
ll.print_list()

# Sort the list using insertion sort
ll.insertion_sort()
print("Sorted list (Insertion Sort):")
ll.print_list()

# Merge two sorted linked lists
ll2 = LinkedList()
ll2.append(0)
ll2.append(5)

print("Second list:")
ll2.print_list()

merged_list = merge_sorted_lists(ll, ll2)
print("Merged sorted list:")
merged_list.print_list()
