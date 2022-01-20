class Stack:

    def __init__(self) -> None:
        self.items = ['Chintamani','Chavan']

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def length(self):
        return len(self.items)

StackObj = Stack()
StackObj.length()
print(StackObj.items)