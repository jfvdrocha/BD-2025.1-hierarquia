from linear_data_structure import LinearDataStructure

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(LinearDataStructure):
    def __init__(self, initial_data=None):
        self._head = None
        self._tail = None
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
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def insert_at_index(self, index, data):
        if not (0 <= index <= self._size):
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_at_start(data)
            return
        if index == self._size:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        current = self._head
        for _ in range(index):
            current = current.next
        
        new_node.next = current
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
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
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        self._size -= 1
        return data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("List is empty")
        data = self._tail.data
        self._tail = self._tail.prev
        if self._tail:
            self._tail.next = None
        else:
            self._head = None
        self._size -= 1
        return data

    def remove_at_index(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_from_start()
        if index == self._size - 1:
            return self.remove_from_end()
        
        current = self._head
        for _ in range(index):
            current = current.next
        
        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self._size -= 1
        return data

    def remove_by_key(self, key):
        current = self._head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev
                self._size -= 1
                return
            current = current.next

    def peek_start(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._head.data

    def peek_end(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._tail.data

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

        # Get nodes at index1 and index2
        node1 = self._head
        for _ in range(index1):
            node1 = node1.next

        node2 = self._head
        for _ in range(index2):
            node2 = node2.next

        # Swap their data
        node1.data, node2.data = node2.data, node1.data

    def bubble_sort(self):
        if self._size < 2:
            return

        for i in range(self._size - 1):
            current = self._head
            for j in range(self._size - 1 - i):
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next

    def __str__(self):
        elements = []
        current = self._head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"


