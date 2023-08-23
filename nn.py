class Value:
    def __init__(self, data,_children=(), _ops=''):
        self.data = data
        self._prev = set(_children)
        self.ops = _ops 
        self.grad = 0.0
    def __repr__(self):
        return f"Value(data={self.data})"
    def __add__(self, other):
        return (Value(self.data + other.data), other, '+')
    def __mul__(self, other):
        return (Value(self.data * other.data), other, '*')

    

a = Value(3.0)
b = Value(1.0)

print(a+b)

