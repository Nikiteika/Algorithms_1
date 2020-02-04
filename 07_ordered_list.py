class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2

    def add(self, value):
        if self.__ascending:
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if self.compare(newNode.value, self.tail.value) == 1:
                    self.tail.next = newNode
                    newNode.prev = self.tail
                    self.tail = newNode
                else:
                    curr = self.head
                    while curr is not None:
                        if self.compare(newNode.value, curr.value) == 0 or self.compare(newNode.value,
                                                                                        curr.value) == -1:
                            if curr == self.head:
                                newNode.next = curr
                                curr.prev = newNode
                                self.head = newNode
                            else:
                                curr.prev.next = newNode
                                newNode.prev = curr.prev
                                newNode.next = curr
                                curr.prev = newNode
                            break
                        curr = curr.next
        else:
            newNode = Node(value)
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                if self.compare(newNode.value, self.tail.value) == -1:
                    self.tail.next = newNode
                    newNode.prev = self.tail
                    self.tail = newNode
                else:
                    curr = self.head
                    while curr is not None:
                        if self.compare(newNode.value, curr.value) == 0 or self.compare(newNode.value,
                                                                                        curr.value) == 1:
                            if curr == self.head:
                                newNode.next = curr
                                curr.prev = newNode
                                self.head = newNode
                            else:
                                curr.prev.next = newNode
                                newNode.prev = curr.prev
                                newNode.next = curr
                                curr.prev = newNode
                            break
                        curr = curr.next
        # автоматическая вставка value
        # в нужную позицию

    def find(self, val):
        node = self.head
        if self.__ascending:
            while node is not None:
                if node.value == val:
                    return node
                if node.value > val:
                    return None
                node = node.next
        else:
            while node is not None:
                if node.value == val:
                    return node
                if node.value < val:
                    return None
                node = node.next
        return None

    def delete(self, val):
        curr = self.head
        if self.__ascending:
            while curr is not None:
                if curr.value == val:
                    if curr == self.head:
                        if curr.next is None:
                            self.head = None
                            self.tail = None
                            return
                        curr.next.prev = None
                        self.head = curr.next
                        return
                    else:
                        if curr == self.tail:
                            curr.prev.next = None
                            self.tail = curr.prev
                            return
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        return
                if curr.value > val:
                    return
                curr = curr.next
        else:
            while curr is not None:
                if curr.value == val:
                    if curr == self.head:
                        if curr.next is None:
                            self.head = None
                            self.tail = None
                            return
                        curr.next.prev = None
                        self.head = curr.next
                        return
                    else:
                        if curr == self.tail:
                            curr.prev.next = None
                            self.tail = curr.prev
                            return
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        return
                if curr.value < val:
                    return
                curr = curr.next
        # здесь будет ваш код

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        k = 0
        while node is not None:
            k += 1
            node = node.next
        return k
        # здесь будет ваш код

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node.value)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if v1.strip() < v2.strip():
            return -1
        elif v1.strip() == v2.strip():
            return 0
        else:
            return 1
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
        # переопределённая версия для строк
