import unittest
from linear_data_structure import LinearDataStructure
from array_class import Array
from singly_linked_list import SinglyLinkedList
from stack_with_linked_list import Pilha, PilhaCheiaErro, PilhaVaziaErro, TipoErro
from doubly_linked_list import DoublyLinkedList
from queue_class import Queue, FilaVaziaErro
from circular_singly_linked_list import CircularSinglyLinkedList
from bandejao_queue_problem import BandejaoQueue, User
from geometric_figures_problem import Point, GeometricFigure
import datetime

class TestArray(unittest.TestCase):
    def test_initialization(self):
        arr = Array(5)
        self.assertEqual(len(arr), 0)
        self.assertTrue(arr.is_empty())
        self.assertFalse(arr.is_full())

    def test_insert_at_end(self):
        arr = Array()
        arr.insert_at_end(1)
        arr.insert_at_end(2)
        self.assertEqual(len(arr), 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)

    def test_insert_at_start(self):
        arr = Array()
        arr.insert_at_start(1)
        arr.insert_at_start(2)
        self.assertEqual(len(arr), 2)
        self.assertEqual(arr[0], 2)
        self.assertEqual(arr[1], 1)

    def test_insert_at_index(self):
        arr = Array(initial_data=[1, 2, 3])
        arr.insert_at_index(1, 99)
        self.assertEqual(len(arr), 4)
        self.assertEqual(arr[1], 99)
        self.assertEqual(str(arr), "[1, 99, 2, 3]")

    def test_remove_from_start(self):
        arr = Array(initial_data=[1, 2, 3])
        self.assertEqual(arr.remove_from_start(), 1)
        self.assertEqual(len(arr), 2)
        self.assertEqual(str(arr), "[2, 3]")

    def test_remove_from_end(self):
        arr = Array(initial_data=[1, 2, 3])
        self.assertEqual(arr.remove_from_end(), 3)
        self.assertEqual(len(arr), 2)
        self.assertEqual(str(arr), "[1, 2]")

    def test_remove_at_index(self):
        arr = Array(initial_data=[1, 2, 3])
        self.assertEqual(arr.remove_at_index(1), 2)
        self.assertEqual(len(arr), 2)
        self.assertEqual(str(arr), "[1, 3]")

    def test_update_at_index(self):
        arr = Array(initial_data=[1, 2, 3])
        arr.update_at_index(1, 99)
        self.assertEqual(arr[1], 99)

    def test_peek_start_end_index(self):
        arr = Array(initial_data=[1, 2, 3])
        self.assertEqual(arr.peek_start(), 1)
        self.assertEqual(arr.peek_end(), 3)
        self.assertEqual(arr.peek_at_index(1), 2)

    def test_bubble_sort(self):
        arr = Array(initial_data=[3, 1, 4, 1, 5, 9, 2, 6])
        arr.bubble_sort()
        self.assertEqual(str(arr), "[1, 1, 2, 3, 4, 5, 6, 9]")

    def test_dynamic_resize(self):
        arr = Array(1)
        arr.insert_at_end(1)
        arr.insert_at_end(2)
        self.assertEqual(len(arr), 2)
        self.assertTrue(arr._capacity >= 2)

class TestSinglyLinkedList(unittest.TestCase):
    def test_initialization(self):
        ll = SinglyLinkedList()
        self.assertTrue(ll.is_empty())
        self.assertEqual(len(ll), 0)

    def test_insert_at_start(self):
        ll = SinglyLinkedList()
        ll.insert_at_start(1)
        ll.insert_at_start(2)
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.peek_start(), 2)
        self.assertEqual(str(ll), "[2, 1]")

    def test_insert_at_end(self):
        ll = SinglyLinkedList()
        ll.insert_at_end(1)
        ll.insert_at_end(2)
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.peek_end(), 2)
        self.assertEqual(str(ll), "[1, 2]")

    def test_insert_at_index(self):
        ll = SinglyLinkedList(initial_data=[1, 2, 3])
        ll.insert_at_index(1, 99)
        self.assertEqual(len(ll), 4)
        self.assertEqual(ll.peek_at_index(1), 99)
        self.assertEqual(str(ll), "[1, 99, 2, 3]")

    def test_remove_from_start(self):
        ll = SinglyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(ll.remove_from_start(), 1)
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[2, 3]")

    def test_remove_from_end(self):
        ll = SinglyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(ll.remove_from_end(), 3)
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[1, 2]")

    def test_remove_at_index(self):
        ll = SinglyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(ll.remove_at_index(1), 2)
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), "[1, 3]")

    def test_update_at_index(self):
        ll = SinglyLinkedList(initial_data=[1, 2, 3])
        ll.update_at_index(1, 99)
        self.assertEqual(ll.peek_at_index(1), 99)

    def test_bubble_sort(self):
        ll = SinglyLinkedList(initial_data=[3, 1, 4, 1, 5, 9, 2, 6])
        ll.bubble_sort()
        self.assertEqual(str(ll), "[1, 1, 2, 3, 4, 5, 6, 9]")

class TestPilha(unittest.TestCase):
    def test_integer_stack(self):
        stack = Pilha("i")
        stack.empilha(1)
        stack.empilha(2)
        self.assertEqual(stack.tamanho(), 2)
        self.assertFalse(stack.pilha_esta_vazia())
        self.assertEqual(stack.desempilha(), 2)
        self.assertEqual(stack.desempilha(), 1)
        self.assertTrue(stack.pilha_esta_vazia())

    def test_char_stack(self):
        stack = Pilha("u")
        stack.empilha("a")
        stack.empilha("b")
        self.assertEqual(stack.tamanho(), 2)
        self.assertEqual(stack.desempilha(), "b")

    def test_empty_stack_error(self):
        stack = Pilha("i")
        with self.assertRaises(PilhaVaziaErro):
            stack.desempilha()

    def test_type_error(self):
        stack = Pilha("i")
        with self.assertRaises(TipoErro):
            stack.empilha("a")

    def test_troca(self):
        stack = Pilha("i")
        stack.empilha(1)
        stack.empilha(2)
        stack.empilha(3)
        stack.troca()
        self.assertEqual(stack.desempilha(), 2)
        self.assertEqual(stack.desempilha(), 3)
        self.assertEqual(stack.desempilha(), 1)

class TestDoublyLinkedList(unittest.TestCase):
    def test_initialization(self):
        dll = DoublyLinkedList()
        self.assertTrue(dll.is_empty())
        self.assertEqual(len(dll), 0)

    def test_insert_at_start(self):
        dll = DoublyLinkedList()
        dll.insert_at_start(1)
        dll.insert_at_start(2)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.peek_start(), 2)
        self.assertEqual(dll.peek_end(), 1)
        self.assertEqual(str(dll), "[2, 1]")

    def test_insert_at_end(self):
        dll = DoublyLinkedList()
        dll.insert_at_end(1)
        dll.insert_at_end(2)
        self.assertEqual(len(dll), 2)
        self.assertEqual(dll.peek_start(), 1)
        self.assertEqual(dll.peek_end(), 2)
        self.assertEqual(str(dll), "[1, 2]")

    def test_insert_at_index(self):
        dll = DoublyLinkedList(initial_data=[1, 2, 3])
        dll.insert_at_index(1, 99)
        self.assertEqual(len(dll), 4)
        self.assertEqual(dll.peek_at_index(1), 99)
        self.assertEqual(str(dll), "[1, 99, 2, 3]")

    def test_remove_from_start(self):
        dll = DoublyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(dll.remove_from_start(), 1)
        self.assertEqual(len(dll), 2)
        self.assertEqual(str(dll), "[2, 3]")

    def test_remove_from_end(self):
        dll = DoublyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(dll.remove_from_end(), 3)
        self.assertEqual(len(dll), 2)
        self.assertEqual(str(dll), "[1, 2]")

    def test_remove_at_index(self):
        dll = DoublyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(dll.remove_at_index(1), 2)
        self.assertEqual(len(dll), 2)
        self.assertEqual(str(dll), "[1, 3]")

    def test_update_at_index(self):
        dll = DoublyLinkedList(initial_data=[1, 2, 3])
        dll.update_at_index(1, 99)
        self.assertEqual(dll.peek_at_index(1), 99)

    def test_bubble_sort(self):
        dll = DoublyLinkedList(initial_data=[3, 1, 4, 1, 5, 9, 2, 6])
        dll.bubble_sort()
        self.assertEqual(str(dll), "[1, 1, 2, 3, 4, 5, 6, 9]")

class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertTrue(q.is_empty())

    def test_peek(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.peek(), 1)
        self.assertEqual(len(q), 2)

    def test_empty_queue_error(self):
        q = Queue()
        with self.assertRaises(FilaVaziaErro):
            q.dequeue()
        with self.assertRaises(FilaVaziaErro):
            q.peek()

class TestCircularSinglyLinkedList(unittest.TestCase):
    def test_initialization(self):
        cll = CircularSinglyLinkedList()
        self.assertTrue(cll.is_empty())
        self.assertEqual(len(cll), 0)

    def test_insert_at_end(self):
        cll = CircularSinglyLinkedList()
        cll.insert_at_end(1)
        cll.insert_at_end(2)
        self.assertEqual(len(cll), 2)
        self.assertEqual(cll.peek_start(), 1)
        self.assertEqual(cll.peek_end(), 2)
        self.assertEqual(str(cll), "[1, 2]")

    def test_insert_at_start(self):
        cll = CircularSinglyLinkedList()
        cll.insert_at_start(1)
        cll.insert_at_start(2)
        self.assertEqual(len(cll), 2)
        self.assertEqual(cll.peek_start(), 2)
        self.assertEqual(cll.peek_end(), 1)
        self.assertEqual(str(cll), "[2, 1]")

    def test_remove_from_start(self):
        cll = CircularSinglyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(cll.remove_from_start(), 1)
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[2, 3]")

    def test_remove_from_end(self):
        cll = CircularSinglyLinkedList(initial_data=[1, 2, 3])
        self.assertEqual(cll.remove_from_end(), 3)
        self.assertEqual(len(cll), 2)
        self.assertEqual(str(cll), "[1, 2]")

    def test_bubble_sort(self):
        cll = CircularSinglyLinkedList(initial_data=[3, 1, 4, 1, 5, 9, 2, 6])
        cll.bubble_sort()
        self.assertEqual(str(cll), "[1, 1, 2, 3, 4, 5, 6, 9]")

class TestBandejaoQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        bq = BandejaoQueue(avg_service_time_per_user_minutes=1)
        bq.enqueue_user("UserA")
        bq.enqueue_user("UserB")
        self.assertEqual(len(bq.queue), 2)
        user_a = bq.dequeue_user()
        self.assertEqual(user_a.user_id, "UserA")
        self.assertEqual(len(bq.queue), 1)

    def test_estimated_wait_time(self):
        bq = BandejaoQueue(avg_service_time_per_user_minutes=1)
        bq.enqueue_user("UserA")
        self.assertEqual(bq.get_estimated_wait_time(), 1)
        bq.enqueue_user("UserB")
        self.assertEqual(bq.get_estimated_wait_time(), 2)

    def test_cancel_user(self):
        bq = BandejaoQueue(avg_service_time_per_user_minutes=1)
        bq.enqueue_user("UserA")
        bq.enqueue_user("UserB")
        bq.cancel_user("UserA")
        self.assertEqual(len(bq.queue), 1)
        self.assertEqual(bq.queue.peek().user_id, "UserB")

    def test_adjust_times(self):
        bq = BandejaoQueue(avg_service_time_per_user_minutes=1)
        bq.enqueue_user("UserA")
        initial_pickup_time = bq.queue.peek().estimated_pickup_time
        bq.adjust_times(5)
        adjusted_pickup_time = bq.queue.peek().estimated_pickup_time
        self.assertEqual(adjusted_pickup_time, initial_pickup_time + datetime.timedelta(minutes=5))

class TestGeometricFigures(unittest.TestCase):
    def test_point_creation(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_figure_creation_and_add_vertex(self):
        fig = GeometricFigure("Test")
        fig.add_vertex(Point(0, 0))
        fig.add_vertex(Point(1, 1))
        self.assertEqual(len(fig.vertices), 2)

    def test_calculate_perimeter_triangle(self):
        fig = GeometricFigure("Triangle")
        fig.add_vertex(Point(0, 0))
        fig.add_vertex(Point(3, 0))
        fig.add_vertex(Point(0, 4))
        # Sides are 3, 4, 5. Perimeter should be 12.
        self.assertAlmostEqual(fig.calculate_perimeter(), 12.0, places=2)

    def test_calculate_perimeter_square(self):
        fig = GeometricFigure("Square")
        fig.add_vertex(Point(0, 0))
        fig.add_vertex(Point(5, 0))
        fig.add_vertex(Point(5, 5))
        fig.add_vertex(Point(0, 5))
        # Sides are 5, 5, 5, 5. Perimeter should be 20.
        self.assertAlmostEqual(fig.calculate_perimeter(), 20.0, places=2)

if __name__ == '__main__':
    unittest.main(argv=["first-arg-is-ignored"], exit=False)


