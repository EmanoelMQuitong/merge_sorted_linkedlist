class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def merge_sort(list, list1):
        merged_list = LinkedList()

        current_node_1 = list.head
        current_node_2 = list1.head

        while current_node_1 is not None or current_node_2 is not None:
            if current_node_1 is not None:
                merged_list.insert_at_end(current_node_1.data)
                current_node_1 = current_node_1.next

            if current_node_2 is not None:
                merged_list.insert_at_end(current_node_2.data)
                current_node_2 = current_node_2.next
        
        return merged_list
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def printLinkedList(self):
        current_node = self.head
        linked_list_str = ""
        while current_node:
            linked_list_str += str(current_node.data)
            if current_node.next:
                linked_list_str += "->"
            current_node = current_node.next
        print(linked_list_str)  
    

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        middle = self._find_middle()
        left_half = LinkedList()
        right_half = LinkedList()

        left_half.head = self.head
        left_half.tail = middle
        right_half.head = middle.next
        middle.next = None

        left_half.merge_sort()
        right_half.merge_sort()

        self.head = self._merge(left_half.head, right_half.head)
    
    def _find_middle(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def _merge(self, left, right):
        temporary = Node(0)
        current = temporary

        while left and right:
            if left.data < right.data:
                current.next = left
                left = left.next
            
            else:
                current.next = right
                right = right.next

            current = current.next

        current.next = left or right

        return temporary.next


# Example usage:
linked_list = LinkedList()
linked_list.insert_at_beginning(2)
linked_list.insert_at_end(4)
linked_list.insert_at_end(6)
linked_list.insert_at_end(8)
linked_list.insert_at_end(10)
linked_list.insert_at_end(12)
print("\n")
print("Sorted Linked List 1: ")
linked_list.printLinkedList()
print("\n")



linked_list1 = LinkedList()
linked_list1.insert_at_beginning(1)
linked_list1.insert_at_end(3)
linked_list1.insert_at_end(5)
linked_list1.insert_at_end(7)
linked_list1.insert_at_end(9)
linked_list1.insert_at_end(11)
print("\n")
print("Sorted Linked List 2: ")
linked_list1.printLinkedList()
print("\n")


# Sort each linked list
linked_list.merge_sort()
linked_list1.merge_sort()

# Merge the sorted linked lists
merged_list = LinkedList()
merged_list.head = merged_list._merge(linked_list.head, linked_list1.head)
print("\n")
print("Merged Lists: ")
merged_list.printLinkedList()
print("\n")


