class TVector2D:
    def __init__(self, x=0, y =0, *args):
        self.x = x
        self.y = y
        self.vector = list(args)

    def __getitem__(self, item):
        if item == 1:
            return self.x
        elif item == 2:
            return self.y
        elif item == 3:
            return self.vector
        else:
            raise Exception("Wrong key")

    def vectors_len(self):
        return len(self.vector)
    def rationing_vector(self):
        return self.x/self.vectors_len(),self.y/self.vectors_len()

    def __gt__(self, other):
        return self.vectors_len() > other.vectors_len()
    def __lt__(self, other):
        return self.vectors_len() < other.vectors_len()
    def __add__(self, other):
        return (other.x + self.x , other.y + self.y)
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return (self.x *other.x + self.y * other.y)


v = TVector2D(7,1, 1,5,7)
v2 = TVector2D(10,4,5,9,1)
print(v + v2)
print(v.vector)
print(v.rationing_vector())
