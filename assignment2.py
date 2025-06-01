class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints the entire linked list."""
        if not self.head:
            print("Linked List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node (1-based index)."""
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index should be a positive integer (1-based).")

        if n == 1:
            print(f"Deleting node at position {n} with value: {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        count = 1

        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value: {current.next.data}")
        current.next = current.next.next


# === Sample Test Case ===
if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()

    # Add nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Original Linked List:")
    ll.print_list()

    # Delete a node
    try:
        ll.delete_nth_node(3)  # Deletes the node with value 30
        print("\nAfter deleting 3rd node:")
        ll.print_list()
    except Exception as e:
        print("Error:", e)

    # Attempt to delete out-of-range
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("\nError:", e)

    # Attempt to delete from empty list
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except Exception as e:
        print("\nError:", e)
