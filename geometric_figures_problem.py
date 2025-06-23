from circular_singly_linked_list import CircularSinglyLinkedList
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

class GeometricFigure:
    def __init__(self, name):
        self.name = name
        self.vertices = CircularSinglyLinkedList()

    def add_vertex(self, point):
        # For simplicity, this implementation does not check for self-intersections
        # when adding points. A more robust solution would require complex geometric algorithms.
        self.vertices.insert_at_end(point)

    def calculate_perimeter(self):
        if len(self.vertices) < 2:
            return 0

        perimeter = 0
        current = self.vertices._head
        for _ in range(len(self.vertices)):
            next_node = current.next
            distance = math.sqrt((next_node.data.x - current.data.x)**2 + (next_node.data.y - current.data.y)**2)
            perimeter += distance
            current = current.next
        return perimeter

    def __str__(self):
        return f"Figure: {self.name}, Vertices: {self.vertices}"


if __name__ == "__main__":
    # Example Usage
    figure1 = GeometricFigure("Triangle")
    figure1.add_vertex(Point(0, 0))
    figure1.add_vertex(Point(3, 0))
    figure1.add_vertex(Point(0, 4))
    print(figure1)
    print(f"Perimeter: {figure1.calculate_perimeter():.2f}")

    figure2 = GeometricFigure("Square")
    figure2.add_vertex(Point(0, 0))
    figure2.add_vertex(Point(5, 0))
    figure2.add_vertex(Point(5, 5))
    figure2.add_vertex(Point(0, 5))
    print(figure2)
    print(f"Perimeter: {figure2.calculate_perimeter():.2f}")

    # Example of a list of figures
    list_of_figures = CircularSinglyLinkedList()
    list_of_figures.insert_at_end(figure1)
    list_of_figures.insert_at_end(figure2)

    print("\nList of Figures:")
    current_figure_node = list_of_figures._head
    for _ in range(len(list_of_figures)):
        print(current_figure_node.data)
        current_figure_node = current_figure_node.next


