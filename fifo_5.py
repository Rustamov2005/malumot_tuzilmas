class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

queue = Queue()
#bo'sh list hosil qilish
queue.items
print(queue.items)
#listning bo'sh yoki bo'sh emasligini tekshirish
queue.is_empty()
print(queue.is_empty())
#listning boshiga element qo'shish
queue.enqueue(87)
queue.enqueue(26)
print(queue.items)
#listning boshidan element o'chirish
queue.dequeue()
print(queue.items)
#Listnig boshidagi elementini o'chirmasdan ko'rish
queue.enqueue(24)
queue.peek()
print(queue.items)
#Listning uzunligini ko'rish
queue.size()
print(f"Listning uzunligi: {queue.size()}")
