class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.massiv = [0] * self.filter_len
        # создаём битовый массив длиной f_len ...


    def hash1(self, str1):
        n = 17
        res = 0
        for c in str1:
            res = res * n + ord(c)
        res = res % self.filter_len
        return res
        # реализация ...

    def hash2(self, str1):
        n = 223
        res = 0
        for c in str1:
            res = res * n + ord(c)
        res = res % self.filter_len
        return res
        # ...

    def add(self, str1):
        self.massiv[self.hash1(str1)] = 1
        self.massiv[self.hash2(str1)] = 1
        # добавляем строку str1 в фильтр

    def is_value(self, str1):
        if self.massiv[self.hash1(str1)] == 1 and self.massiv[self.hash2(str1)] == 1:
            return True
        else:
            return False
        # проверка, имеется ли строка str1 в фильтре
