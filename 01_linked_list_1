class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        print('[. ', end='')
        while node is not None:
            print(node.value, end=' ')  # end=' ' - можно добавить, чтобы выводил в строку
            node = node.next
        print('.]', end='\n')

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        lst = []
        while node is not None:
            if node.value == val:
                lst.append(node)
            node = node.next
        return lst

    def delete(self, val, all=False):
        prev = None
        curr = self.head
        if not all:
            while curr is not None:
                if curr.value == val:
                    if prev is not None:
                        prev.next = curr.next
                        if curr.next is None:
                            self.tail = prev
                        break
                    else:
                        self.head = curr.next
                        if self.head is None:
                            self.tail = None
                        break
                prev = curr
                curr = curr.next
        else:
            while curr is not None:
                if curr.value == val:
                    if prev is not None:
                        prev.next = curr.next
                        if curr.next is None:
                            self.tail = prev
                        curr = prev.next
                    else:
                        self.head = curr.next
                        if self.head is None:
                            self.tail = None
                        curr = self.head
                else:
                    prev = curr
                    curr = curr.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        k = 0
        while node is not None:
            k += 1
            node = node.next
        return k

    def insert(self, afterNode, newNode):
        if self.head is None:
            if afterNode is None:
                newNode.next = self.head
                self.head = newNode
                self.tail = newNode
            else:
                return None
            return None
        else:
            if afterNode is None:
                newNode.next = self.head
                self.head = newNode
            else:
                node = self.head
                while node is not None:
                    if node.value == afterNode.value:
                        if node.next is None:
                            self.tail.next = newNode
                            self.tail = newNode
                        else:
                            newNode.next = node.next
                            node.next = newNode
                        return
                    node = node.next
            return None

def compare(x, y):
    if x.len() == y.len():
        nodex = x.head
        nodey = y.head
        lst = []
        while nodex is not None and nodey is not None:
            lst.append(nodex.value + nodey.value)
            nodex = nodex.next
            nodey = nodey.next
        return lst
    else:
        return 'Длины не равны'
