class PowerSet:

    def __init__(self, stp=3, sz=20000):
        self.sz = sz
        self.step = stp
        self.slots = [None] * self.sz
        # ваша реализация хранилища

    def hash_fun(self, value):
        # в качестве value поступают строки!
        value = str(value)
        slot = 0
        for i in range(len(value)):
            slot += ord(value[i]) * (i + 1) + i
        slot = slot % self.sz
        # всегда возвращает корректный индекс слота
        return slot

    def seek_slot(self, value):
        hesh = self.hash_fun(value)
        if self.slots[hesh] is None:
            return hesh
        else:
            a = (hesh + self.step) % self.sz
            for k in range(self.sz + 1):
                if self.slots[a] is None:
                    return a
                a = (a + self.step) % self.sz
            return None
        # находит индекс пустого слота для значения, или None

    def find(self, value):
        if value in self.slots:
            return self.slots.index(value)
        else:
            return None
        # находит индекс слота со значением, или None

    def size(self):
        count = 0
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                count += 1
        return count
        # количество элементов в множестве

    def get(self, value):
        if self.find(value) is not None:
            return True
        else:
            return False
        # возвращает True если value имеется в множестве,
        # иначе False

    def put(self, value):
        # записываем значение по хэш-функции
        is_in = self.find(value)
        if is_in is None:
            slot = self.seek_slot(value)
            if slot is not None:
                self.slots[slot] = value
                return slot
            else:
                return None
        else:
            return None
        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить

    def remove(self, value):
        is_in = self.find(value)
        if is_in is not None:
            self.slots[is_in] = None
            return True
        else:
            return False
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        elem_1 = self.slots
        elem_2 = set2.slots
        setC = PowerSet()
        for i in range(len(elem_1)):
            if elem_1[i] is not None and elem_1[i] in elem_2:
                setC.put(elem_1[i])
        # пересечение текущего множества и set2
        return setC

    def union(self, set2):
        elem_1 = self.slots
        elem_2 = set2.slots
        setC = PowerSet()
        for i in range(len(elem_1)):
            if elem_1[i] is not None:
                setC.put(elem_1[i])
        for i in range(len(elem_2)):
            if elem_2[i] is not None and elem_2[i] not in elem_1:
                setC.put(elem_2[i])
        # объединение текущего множества и set2
        return setC

    def difference(self, set2):
        elem_1 = self.slots
        elem_2 = set2.slots
        setC = PowerSet()
        for i in range(len(elem_1)):
            if elem_1[i] is not None and elem_1[i] not in elem_2:
                setC.put(elem_1[i])
        # разница текущего множества и set2
        return setC

    def issubset(self, set2):
        elem_1 = self.slots
        elem_2 = set2.slots
        count = 0
        for i in range(len(elem_2)):
            if elem_2[i] is not None and elem_2[i] in elem_1:
                count += 1
        if set2.size() == count:
            return True
        else:
            return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
