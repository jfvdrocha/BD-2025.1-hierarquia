from singly_linked_list import SinglyLinkedList

class FilaVaziaErro(Exception): pass

class Queue:
    def __init__(self):
        self._list = SinglyLinkedList()

    def enqueue(self, data):
        self._list.insert_at_end(data)

    def dequeue(self):
        if self.is_empty():
            raise FilaVaziaErro("A fila está vazia")
        return self._list.remove_from_start()

    def peek(self):
        if self.is_empty():
            raise FilaVaziaErro("A fila está vazia")
        return self._list.peek_start()

    def is_empty(self):
        return self._list.is_empty()

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return str(self._list)


