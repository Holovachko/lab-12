class Array:
    def __init__(self, *args):
        self.list_1 = list(args)

    def __getitem__(self, key):
        return self.list_1[key-1]

    def __setitem__(self, key, value):
        if key - 1 in range(len(self.list_1)):
            self.list_1[key-1] = value
        else:
            self.list_1.append(value)

    def max_element(self):
        return max(self.list_1)
    def min_element(self):
        return min(self.list_1)


t = Array(12,52,5,39,24)
print(t.__getitem__(2))
t.__setitem__(6,12)
print(t.list_1)
print(t.max_element())
