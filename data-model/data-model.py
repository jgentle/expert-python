"""
Creating Behavior in a Custom Class

The emerging pattern is that for any behavior that you want to implement, you write the __function__ ('dunder methods' aka data model methods) for the class.

Top level function/Syntax ==> Corresponding __function__
Examples.
    x + y ==> __add__

    init x ==>  __init__

    repr(x) ==>     __repr__

The python data model is a means by which you can implement protocols.
These protocols have some abstract meaning depending on the object itself.
Ex. adding polynomials mens what that means in a math class.
Ex. getting its representation means the string required to create another object of that Type.

"""


# v.0 :: Simple polynomial class.
"""
class Polynomial_0:
    pass

p1_0 = Polynomial_0()
p2_0 = Polynomial_0()
p1_0.coeffs = 1, 2, 3     # x2 + 2x  3
p2_0.coeffs = 3, 4, 3     # 3x2 + 4x + 3
"""

"""
Run interactively:
$ python -i data-model.py
>>>
"""


# v.1 :: Improved Polynomial class.
"""
class Polynomial_1:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

p1_1 = Polynomial_1(1, 2, 3)      # x2 + 2x  3
p2_1 = Polynomial_1(3, 4, 3)      # 3x2 + 4x + 3
"""

"""
>>> p1_0
<__main__.Polynomial_0 instance at 0x107eae2d8>
>>> p1_1
<__main__.Polynomial_1 instance at 0x107eae368>
>>> p2_0
<__main__.Polynomial_0 instance at 0x107eae320>
>>> p2_1
<__main__.Polynomial_1 instance at 0x107eae3b0>
"""


# v.2 :: Enhanced polynomial class - repr method.
"""
class Polynomial_2:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial_2(*{!r})'.format(self.coeffs)

p1_2 = Polynomial_2(1, 2, 3)      # x2 + 2x  3
p2_2 = Polynomial_2(3, 4, 3)      # 3x2 + 4x + 3
"""

"""
>>> p1_2
Polynomial_2(*(1, 2, 3))
>>> p2_2
Polynomial_2(*(3, 4, 3))
"""


# v.3 :: Enhanced polynomial class - add method.
"""
class Polynomial_3:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial_2(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial_3(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

p1_3 = Polynomial_3(1, 2, 3)      # x2 + 2x  3
p2_3 = Polynomial_3(3, 4, 3)      # 3x2 + 4x + 3
"""

"""
>>> p1_3 + p2_3
Polynomial_2(*(4, 6, 6))
"""


# v.4 :: Enhanced polynomial class - add len.
# """
class Polynomial_4:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial_2(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial_3(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

p1_4 = Polynomial_4(1, 2, 3)      # x2 + 2x  3
p2_4 = Polynomial_4(3, 4, 3)      # 3x2 + 4x + 3
# """

"""
>>> len(p1_4)
3
>>> len(p2_4)
3
"""
