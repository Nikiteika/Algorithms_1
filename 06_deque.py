class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        if len(self.deque) == 0:
            self.deque.append(item)
        else:
            self.deque = [item] + self.deque

    def addTail(self, item):
        self.deque.append(item)
        # добавление в хвост

    def removeFront(self):
        if len(self.deque) != 0:
            return self.deque.pop(0)
        else:
            return None

    def removeTail(self):
        if len(self.deque) != 0:
            return self.deque.pop()
        else:
            return None

    def size(self):
        return len(self.deque)
