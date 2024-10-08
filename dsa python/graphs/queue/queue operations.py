class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
        print(f"Enqueued {data} to the front of the queue.")

    def dequeue(self):
        if self.queue:
            element = self.queue.pop()
            print(f"Dequeued {element} from the queue.")
            return element
        else:
            print("Queue is empty, cannot dequeue.")

    def is_empty(self):
        return not self.queue

    def size(self):
        return len(self.queue)

    def display(self):
        if self.queue:
            print("Queue:", " <- ".join(map(str, self.queue)))
        else:
            print("Queue is currently empty.")

def main():
    q = Queue()
    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Check if Empty")
        print("5. Size of Queue")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            data = input("Enter element to enqueue: ")
            q.enqueue(data)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            q.display()
        elif choice == '4':
            if q.is_empty():
                print("The queue is empty.")
            else:
                print("The queue is not empty.")
        elif choice == '5':
            print(f"Size of the queue: {q.size()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
