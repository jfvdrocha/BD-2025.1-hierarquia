from linear_data_structure import LinearDataStructure

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList(LinearDataStructure):
    def __init__(self, initial_data=None):
        self._head = None
        self._size = 0

        if initial_data is not None:
            for item in initial_data:
                self.insert_at_end(item)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return False  # Linked list is never full (limited by memory)

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def insert_at_index(self, index, data):
        if not (0 <= index <= self._size):
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_at_start(data)
            return
        
        new_node = Node(data)
        current = self._head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def update_by_key(self, key, new_data):
        current = self._head
        while current:
            if current.data == key:
                current.data = new_data
                return
            current = current.next
        raise ValueError("Key not found")

    def update_at_index(self, index, new_data):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        current = self._head
        for _ in range(index):
            current = current.next
        current.data = new_data

    def remove_from_start(self):
        if self.is_empty():
            raise IndexError("List is empty")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        return data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("List is empty")
        if self._size == 1:
            return self.remove_from_start()
        
        current = self._head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        self._size -= 1
        return data

    def remove_at_index(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_from_start()
        
        current = self._head
        for _ in range(index - 1):
            current = current.next
        data = current.next.data
        current.next = current.next.next
        self._size -= 1
        return data

    def remove_by_key(self, key):
        if self.is_empty():
            return
        if self._head.data == key:
            self.remove_from_start()
            return
        
        current = self._head
        while current.next and current.next.data != key:
            current = current.next
        if current.next:
            current.next = current.next.next
            self._size -= 1

    def peek_start(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._head.data

    def peek_end(self):
        if self.is_empty():
            raise IndexError("List is empty")
        current = self._head
        while current.next:
            current = current.next
        return current.data

    def peek_at_index(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.data

    def find_by_key(self, key):
        current = self._head
        while current:
            if current.data == key:
                return current.data
            current = current.next
        raise ValueError("Key not found")

    def find_next_by_key(self, key, start_index):
        current = self._head
        for _ in range(start_index):
            if current is None:
                raise IndexError("Start index out of bounds")
            current = current.next

        while current:
            if current.data == key:
                return current.data
            current = current.next
        raise ValueError("Key not found from start_index")

    def swap(self, index1, index2):
        if not (0 <= index1 < self._size and 0 <= index2 < self._size):
            raise IndexError("Index out of bounds")
        
        if index1 == index2:
            return

        # Ensure index1 is smaller than index2
        if index1 > index2:
            index1, index2 = index2, index1

        node1_prev = None
        node1 = self._head
        for i in range(index1):
            node1_prev = node1
            node1 = node1.next

        node2_prev = None
        node2 = self._head
        for i in range(index2):
            node2_prev = node2
            node2 = node2.next

        if node1_prev:
            node1_prev.next = node2
        else:
            self._head = node2

        if node2_prev:
            node2_prev.next = node1
        else:
            self._head = node1

        node1.next, node2.next = node2.next, node1.next

    def bubble_sort(self):
        if self._size < 2:
            return

        for i in range(self._size - 1):
            current = self._head
            for j in range(self._size - 1 - i):
                if current.data > current.next.data:
                    # Swap data directly for simplicity in linked list bubble sort
                    current.data, current.next.data = current.next.data, current.data
                current = current.next

    def __str__(self):
        elements = []
        current = self._head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"


