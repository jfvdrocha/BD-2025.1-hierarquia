from linear_data_structure import LinearDataStructure

class Array(LinearDataStructure):
    def __init__(self, capacity=0, initial_data=None):
        self._array = [None] * capacity
        self._size = 0
        self._capacity = capacity

        if initial_data is not None:
            for item in initial_data:
                self.insert_at_end(item)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def _resize(self):
        self._capacity = max(1, self._capacity * 2)
        new_array = [None] * self._capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array

    def insert_at_start(self, data):
        if self.is_full():
            self._resize()
        for i in range(self._size, 0, -1):
            self._array[i] = self._array[i - 1]
        self._array[0] = data
        self._size += 1

    def insert_at_end(self, data):
        if self.is_full():
            self._resize()
        self._array[self._size] = data
        self._size += 1

    def insert_at_index(self, index, data):
        if not (0 <= index <= self._size):
            raise IndexError("Index out of bounds")
        if self.is_full():
            self._resize()
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = data
        self._size += 1

    def update_by_key(self, key, new_data):
        for i in range(self._size):
            if self._array[i] == key:
                self._array[i] = new_data
                return
        raise ValueError("Key not found")

    def update_at_index(self, index, new_data):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        self._array[index] = new_data

    def remove_from_start(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        data = self._array[0]
        for i in range(self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return data

    def remove_from_end(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        data = self._array[self._size - 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return data

    def remove_at_index(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        data = self._array[index]
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1
        return data

    def remove_by_key(self, key):
        try:
            index = self._array.index(key)
            self.remove_at_index(index)
        except ValueError:
            pass # Key not found, do nothing as per requirement

    def peek_start(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        return self._array[0]

    def peek_end(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        return self._array[self._size - 1]

    def peek_at_index(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        return self._array[index]

    def find_by_key(self, key):
        for item in self._array[:self._size]:
            if item == key:
                return item
        raise ValueError("Key not found")

    def find_next_by_key(self, key, start_index):
        for i in range(start_index, self._size):
            if self._array[i] == key:
                return self._array[i]
        raise ValueError("Key not found from start_index")

    def swap(self, index1, index2):
        if not (0 <= index1 < self._size and 0 <= index2 < self._size):
            raise IndexError("Index out of bounds")
        self._array[index1], self._array[index2] = self._array[index2], self._array[index1]

    def bubble_sort(self):
        n = self._size
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self._array[j] > self._array[j + 1]:
                    self.swap(j, j + 1)

    def __getitem__(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        return self._array[index]

    def __setitem__(self, index, value):
        if not (0 <= index < self._size):
            raise IndexError("Index out of bounds")
        self._array[index] = value

    def __str__(self):
        return str(self._array[:self._size])


