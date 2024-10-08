class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def display(self):
        if not self.head:
            print("The list is empty.")
        else:
            temp = self.head.next
            while True:
                print(temp.data, end=" -> ")
                temp = temp.next
                if temp == self.head.next:
                    break
            print("(circular)")

def main():
    clist = CircularLinkedList()
    n = int(input("Enter number of elements: "))
    for _ in range(n):
        data = int(input("Enter data: "))
        clist.insert(data)
    print("\nThe Circular Linked List:")
    clist.display()

if __name__ == "__main__":
    main()
