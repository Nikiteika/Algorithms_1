class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        key = str(key)
        slot = 0
        for i in range(len(key)):
            slot += ord(key[i]) * (i + 1) + i
        slot = slot % self.size
        return slot
        # всегда возвращает корректный индекс слота

    def is_key(self, key):
        # возвращает True если ключ имеется,
        if key in self.slots:
            return True
        else:
            return False
        # иначе False

    def put(self, key, value):  # В методе каждой новой паре КЛЮЧ-ЗНАЧЕНИЕ делаем hits=1,
        try:                    # чтобы отличались от пустых ячеек таблицы
            slot = self.slots.index(key)           # Пытаемся найти НОМЕР элемента с заданным КЛЮЧОМ
        except ValueError:                         # Если ВЫДАЁТ исключение, значит такого КЛЮЧА в таблице нет
            slot = self.hash_fun(key)              # и нам просто нужно внести в таблицу пару КЛЮЧ-ЗНАЧЕНИЕ

            if self.slots[slot] is not None:       # Если случается КОЛЛИЗИЯ, то ищем элемент
                minhits = self.hits[0]             # с минимальным количеством обращений (hits)
                minhitsind = 0

                for i in range(1, self.size):      # Ищем номер элемента с минимальным количеством 'hits'
                    if self.hits[i] < minhits:
                        minhits = self.hits[i]
                        minhitsind = i

                self.slots[minhitsind] = key       # Перезаписываем новую пару КЛЮЧ-ЗНАЧЕНИЕ на место самого
                self.values[minhitsind] = value    # 'ненужного' элемента
                self.hits[minhitsind] = 1
            else:
                self.slots[slot] = key
                self.values[slot] = value
                self.hits[slot] = 1
        else:                                      # Если НЕ ВЫДАЁТ исключение, значит такой КЛЮЧ в таблице есть
            self.values[slot] = value              # И мы просто перезаписываем VALUE (ЗНАЧЕНИЕ)

    def get(self, key):
        try:
            slot = self.slots.index(key)
        except ValueError:
            return None
        else:
            self.hits[slot] += 1
            return self.values[slot]
        # возвращает value для key,
        # или None если ключ не найден
