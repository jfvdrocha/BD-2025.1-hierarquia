from linear_data_structure import LinearDataStructure

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularSinglyLinkedList(LinearDataStructure):
    def __init__(self, initial_data=None, fixed_size=None):
        self._head = None
        self._size = 0
        self._fixed_size = fixed_size

        if initial_data is not None:
            for item in initial_data:
                self.insert_at_end(item)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        if self._fixed_size is None:
            return False
        return self._size >= self._fixed_size

    def insert_at_start(self, data):
        if self.is_full():
            raise IndexError("List is full")
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            new_node.next = self._head
        else:
            current = self._head
            while current.next != self._head:
                current = current.next
            new_node.next = self._head
            self._head = new_node
            current.next = self._head
        self._size += 1

    def insert_at_end(self, data):
        if self.is_full():
            raise IndexError("List is full")
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            new_node.next = self._head
        else:
            current = self._head
            while current.next != self._head:
                current = current.next
            current.next = new_node
            new_node.next = self._head
        self._size += 1

    def insert_at_index(self, index, data):
        if self.is_full():
            raise IndexError("List is full")
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
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def update_by_key(self, key, new_data):
        if self.is_empty():
            raise ValueError("List is empty")
        current = self._head
        for _ in range(self._size):
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
        if self._size == 1:
            self._head = None
        else:
            current = self._head
            while current.next != self._head:
                current = current.next
            self._head = self._head.next
            current.next = self._head
        self._size -= 1
        return data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("List is empty")
        if self._size == 1:
            return self.remove_from_start()
        
        current = self._head
        while current.next.next != self._head:
            current = current.next
        data = current.next.data
        current.next = self._head
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
        prev = None
        for _ in range(self._size - 1):
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                self._size -= 1
                return
        # If key is not found, do nothing as per requirement

    def peek_start(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._head.data

    def peek_end(self):
        if self.is_empty():
            raise IndexError("List is empty")
        current = self._head
        while current.next != self._head:
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
        if self.is_empty():
            raise ValueError("List is empty")
        current = self._head
        for _ in range(self._size):
            if current.data == key:
                return current.data
            current = current.next
        raise ValueError("Key not found")

    def find_next_by_key(self, key, start_index):
        if self.is_empty():
            raise ValueError("List is empty")
        if not (0 <= start_index < self._size):
            raise IndexError("Start index out of bounds")

        current = self._head
        for _ in range(start_index):
            current = current.next

        for _ in range(self._size):
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
        if self.is_empty():
            return "[]"
        elements = []
        current = self._head
        for _ in range(self._size):
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(elements) + "]"


