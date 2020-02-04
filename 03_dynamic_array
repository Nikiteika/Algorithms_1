import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, item):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        elif i == self.count:
            self.append(item)
        else:
            if self.count + 1 > self.capacity:
                self.resize(self.capacity * 2)
            new_array = self.make_array(self.capacity)
            for j in range(i):
                new_array[j] = self.array[j]
            new_array[i] = item
            for j in range(i + 1, self.count + 1):
                new_array[j] = self.array[j - 1]
            self.array = new_array
            self.count += 1

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        else:
            if self.capacity != 16 and self.count - 1 < self.capacity * 0.5:
                if int(self.capacity / 1.5) > 16:
                    self.resize(int(self.capacity / 1.5))
                else:
                    self.resize(16)
            new_array = self.make_array(self.capacity)
            for j in range(i):
                new_array[j] = self.array[j]
            for j in range(i + 1, self.count):
                new_array[j - 1] = self.array[j]
            self.array = new_array
            self.count -= 1
