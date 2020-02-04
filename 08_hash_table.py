class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        slot = len(value)
        for i in range(len(value)):
            slot += ord(value[i]) * (i + 1) + i
        slot = slot % self.size
        # всегда возвращает корректный индекс слота
        return slot

    def seek_slot(self, value):
        hesh = self.hash_fun(value)
        if self.slots[hesh] is None:
            return hesh
        else:
            a = (hesh + self.step) % self.size
            for k in range(self.size + 1):
                if self.slots[a] is None:
                    return a
                a = (a + self.step) % self.size
            return None
        # находит индекс пустого слота для значения, или None

    def put(self, value):
        # записываем значение по хэш-функции
        slot = self.seek_slot(value)
        if slot is not None:
            self.slots[slot] = value
            return slot
        else:
            return None
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить

    def find(self, value):
        hesh = self.hash_fun(value)
        if self.slots[hesh] == value:
            return hesh
        else:
            a = (hesh + self.step) % self.size
            for k in range(self.size + 1):
                if self.slots[a] == value:
                    return a
                a = (a + self.step) % self.size
            return None
        # находит индекс слота со значением, или None
