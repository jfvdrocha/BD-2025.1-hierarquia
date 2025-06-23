import datetime
from queue_class import Queue

class User:
    def __init__(self, user_id, arrival_time):
        self.user_id = user_id
        self.arrival_time = arrival_time
        self.estimated_pickup_time = None
        self.remaining_time = None

    def __str__(self):
        return f"User ID: {self.user_id}, Arrival: {self.arrival_time.strftime('%H:%M:%S')}, Pickup: {self.estimated_pickup_time.strftime('%H:%M:%S') if self.estimated_pickup_time else 'N/A'}, Remaining: {self.remaining_time if self.remaining_time else 'N/A'} min"

class BandejaoQueue:
    def __init__(self, avg_service_time_per_user_minutes=2):
        self.queue = Queue()
        self.avg_service_time_per_user_minutes = avg_service_time_per_user_minutes
        self.current_time = datetime.datetime.now()

    def _calculate_estimated_time(self, queue_size):
        return queue_size * self.avg_service_time_per_user_minutes

    def get_estimated_wait_time(self):
        return self._calculate_estimated_time(len(self.queue))

    def enqueue_user(self, user_id):
        user = User(user_id, datetime.datetime.now())
        estimated_wait = self.get_estimated_wait_time()
        user.estimated_pickup_time = user.arrival_time + datetime.timedelta(minutes=estimated_wait)
        user.remaining_time = estimated_wait
        self.queue.enqueue(user)
        self._update_all_users_times()
        print(f"User {user_id} enqueued. Estimated pickup time: {user.estimated_pickup_time.strftime('%H:%M:%S')}")

    def dequeue_user(self):
        try:
            user = self.queue.dequeue()
            print(f"User {user.user_id} dequeued.")
            self._update_all_users_times()
            return user
        except FilaVaziaErro:
            print("Queue is empty. No user to dequeue.")
            return None

    def cancel_user(self, user_id):
        temp_queue = Queue()
        found = False
        while not self.queue.is_empty():
            user = self.queue.dequeue()
            if user.user_id == user_id:
                found = True
                print(f"User {user_id} cancelled and removed from queue.")
            else:
                temp_queue.enqueue(user)
        self.queue = temp_queue
        if found:
            self._update_all_users_times()
        else:
            print(f"User {user_id} not found in queue.")
        return found

    def _update_all_users_times(self):
        temp_queue = Queue()
        current_estimated_time = 0
        while not self.queue.is_empty():
            user = self.queue.dequeue()
            user.estimated_pickup_time = user.arrival_time + datetime.timedelta(minutes=current_estimated_time + self.avg_service_time_per_user_minutes)
            user.remaining_time = current_estimated_time + self.avg_service_time_per_user_minutes
            temp_queue.enqueue(user)
            current_estimated_time += self.avg_service_time_per_user_minutes
        self.queue = temp_queue

    def adjust_times(self, adjustment_minutes):
        temp_queue = Queue()
        while not self.queue.is_empty():
            user = self.queue.dequeue()
            user.estimated_pickup_time += datetime.timedelta(minutes=adjustment_minutes)
            user.remaining_time += adjustment_minutes
            temp_queue.enqueue(user)
        self.queue = temp_queue
        print(f"Adjusted all users' times by {adjustment_minutes} minutes.")

    def display_queue(self):
        if self.queue.is_empty():
            print("The queue is currently empty.")
            return
        print("\nCurrent Bandejao Queue:")
        temp_queue = Queue()
        while not self.queue.is_empty():
            user = self.queue.dequeue()
            print(user)
            temp_queue.enqueue(user)
        self.queue = temp_queue


if __name__ == "__main__":
    bandejao = BandejaoQueue()

    bandejao.enqueue_user("Alice")
    bandejao.enqueue_user("Bob")
    bandejao.display_queue()

    bandejao.enqueue_user("Charlie")
    bandejao.display_queue()

    bandejao.dequeue_user()
    bandejao.display_queue()

    bandejao.cancel_user("Bob")
    bandejao.display_queue()

    bandejao.adjust_times(5) # Atraso de 5 minutos
    bandejao.display_queue()

    bandejao.adjust_times(-2) # Adiantamento de 2 minutos
    bandejao.display_queue()

    bandejao.cancel_user("David") # Testar usuário não encontrado
    bandejao.display_queue()


