from abc import ABC, abstractmethod

class LinearDataStructure(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def insert_at_start(self, data):
        pass

    @abstractmethod
    def insert_at_end(self, data):
        pass

    @abstractmethod
    def insert_at_index(self, index, data):
        pass

    @abstractmethod
    def update_by_key(self, key, new_data):
        pass

    @abstractmethod
    def update_at_index(self, index, new_data):
        pass

    @abstractmethod
    def remove_from_start(self):
        pass

    @abstractmethod
    def remove_from_end(self):
        pass

    @abstractmethod
    def remove_at_index(self, index):
        pass

    @abstractmethod
    def remove_by_key(self, key):
        pass

    @abstractmethod
    def peek_start(self):
        pass

    @abstractmethod
    def peek_end(self):
        pass

    @abstractmethod
    def peek_at_index(self, index):
        pass

    @abstractmethod
    def find_by_key(self, key):
        pass

    @abstractmethod
    def find_next_by_key(self, key, start_index):
        pass

    @abstractmethod
    def swap(self, index1, index2):
        pass

    @abstractmethod
    def bubble_sort(self):
        pass


