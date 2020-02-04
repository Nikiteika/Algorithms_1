class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        slot = len(key)
        for i in range(len(key)):
            slot += ord(key[i]) * (i + 1) + i
        slot = slot % self.size
        return slot
        # всегда возвращает корректный индекс слота

    def is_key(self, key):
        # возвращает True если ключ имеется,
        for i in range(len(self.slots)):
            if key == self.slots[i]:
                return True
        return False
        # иначе False

    def put(self, key, value):
        if self.is_key(key):
            for i in range(0, len(self.slots)):
                if self.slots[i] == key:
                    slot = i
                    break
            self.values[slot] = value
        else:
            slot = self.hash_fun((key))
            self.slots[slot] = key
            self.values[slot] = value

    def get(self, key):
        if self.is_key(key):
            for i in range(0, len(self.slots)):
                if self.slots[i] == key:
                    return self.values[i]
        else:
            return None
        # возвращает value для key,
        # или None если ключ не найден
