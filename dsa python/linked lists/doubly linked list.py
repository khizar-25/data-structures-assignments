class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> " if temp.next else "\n")
            temp = temp.next

    def display_reverse(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <=> " if temp.prev else "\n")
            temp = temp.prev

def main():
    dll = DoublyLinkedList()
    n = int(input("Enter number of elements: "))
    for _ in range(n):
        data = int(input("Enter data: "))
        dll.insert(data)
    print("\nForward order:")
    dll.display_forward()
    print("\nReverse order:")
    dll.display_reverse()

if __name__ == "__main__":
    main()
