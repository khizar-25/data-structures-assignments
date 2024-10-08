class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("Empty List")
            return
        while current:
            end_symbol = " -> " if current.next else "\n"
            print(current.data, end=end_symbol)
            current = current.next

def main():
    ll = LinkedList()
    for _ in range(int(input("Number of elements: "))):
        ll.insert(int(input("Enter element: ")))
    ll.display()

if __name__ == "__main__":
    main()
