# Syntax

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def list_is_empty(self) -> None:
        return not self.head

if __name__ == '__main__':
    my_linked_list = LinkedList()