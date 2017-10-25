

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
"""
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
"""

"""
>>> len(p1_4)
3
>>> len(p2_4)
3
"""


# v.5 :: Enhanced polynomial class - add call.
# """
class Polynomial_5:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial_2(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial_3(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        print('Called')
        return

p1_5 = Polynomial_5(1, 2, 3)      # x2 + 2x  3
p2_5 = Polynomial_5(3, 4, 3)      # 3x2 + 4x + 3
# """

"""
>>> p1_5()
Called
>>> p2_5()
Called
"""
