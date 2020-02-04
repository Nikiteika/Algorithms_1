class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
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
        lst = []
        node = self.head
        while node is not None:
            if node.value == val:
                lst.append(node)
            node = node.next
        return lst

    def delete(self, val, all=False):
        back = None
        curr = self.head
        if curr is not None and curr.next is not None:
            foll = curr.next
        else:
            foll = None
        if not all:
            while curr is not None:
                if curr.value == val:
                    if back is not None:
                        back.next = foll
                        if foll is None:
                            self.tail = back
                        else:
                            foll.prev = back
                        break
                    else:
                        self.head = foll
                        if self.head is None:
                            self.tail = None
                        else:
                            foll.prev = None
                        break
                back = curr
                curr = curr.next
                if foll is not None:
                    foll = foll.next
        else:
            while curr is not None:
                if curr.value == val:
                    if back is not None:
                        back.next = foll
                        if foll is None:
                            self.tail = back
                        else:
                            foll.prev = back
                        curr = foll
                        if foll is not None:
                            foll = foll.next
                    else:
                        self.head = foll
                        if self.head is None:
                            self.tail = None
                            curr = foll
                        else:
                            foll.prev = None
                            curr = foll
                            foll = foll.next
                else:
                    back = curr
                    curr = curr.next
                    if foll is not None:
                        foll = foll.next

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
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node.value == afterNode.value:
                    if node.next is None:
                        self.tail.next = newNode
                        newNode.prev = self.tail
                        self.tail = newNode
                    else:
                        node.next.prev = newNode
                        newNode.next = node.next
                        newNode.prev = node
                        node.next = newNode
                    return
                node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            node = self.head
            node.prev = newNode
            newNode.next = node
            self.head = newNode
