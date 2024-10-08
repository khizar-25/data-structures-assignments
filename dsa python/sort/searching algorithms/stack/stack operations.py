class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"{data} pushed onto stack.")

    def pop(self):
        if not self.is_empty():
            removed_element = self.stack.pop()
            print(f"{removed_element} popped from stack.")
            return removed_element
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top element is {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        if not self.is_empty():
            print("Current Stack:", " -> ".join(map(str, reversed(self.stack))))
        else:
            print("Stack is empty.")

def main():
    stack = Stack()
    while True:
        print("\nChoose a stack operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Check if empty")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter the element to push: "))
            stack.push(data)

        elif choice == 2:
            stack.pop()

        elif choice == 3:
            stack.peek()

        elif choice == 4:
            stack.display()

        elif choice == 5:
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
