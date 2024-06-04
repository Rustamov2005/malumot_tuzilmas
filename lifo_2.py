

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)


stack = Stack()
#bo'sh yoki bo'sh emasligini tekshirish
stack.is_empty()
print(stack.is_empty())
#oxiriga element qo'shish
stack.push(11)
stack.push(21)
print(stack.items)
#oxiridan element o'chirib yuborish
stack.pop()
print(stack.pop())
#boshidagi elementbi olibtashlamasdan ko'rish
stack.push(15)
stack.push(26)
stack.peek()
print(stack.peek())
#o'lchamini ko'rish
stack.size()
print(f"Listning uzunligi: {stack.size()}")

