"""

    Implement the sub method for the Vector class of Section 2.3.3, so
    that the expression u−v returns a new vector instance representing the
    difference between two vectors.

================================================================================================
    
    Implement the neg method for the Vector class of Section 2.3.3, so
    that the expression −v returns a new vector instance whose coordinates
    are all the negated values of the respective coordinates of v.

================================================================================================

    In Section 2.3.3, we note that our Vector class supports a syntax such as
    v=u+[5,3,10,−2, 1], in which the sum of a vector and list returns
    a new vector. However, the syntax v=[5,3,10,−2, 1] + u is illegal.
    Explain how the Vector class definition can be revised so that this syntax
    generates a new vector.

"""

class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        
        result = Vector(len(self))
        
        for j in range(len(self)):
            result[j] = self[j] + other[j]  
        
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        
        result = Vector(len(self))
        
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        
        return result

    def __mul__(self, d):
        pass

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other
        
    def __neg__(self):
        result = Vector(len(self))
        
        for j in range(len(self)):
            result[j] = -self[j]
        
        return result

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

v = Vector(3)
v[0], v[1], v[2] = 1, -2, 3

neg_v = -v
print(neg_v)  # Debería imprimir: <-1, 2, -3>
