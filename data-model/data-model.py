
"""
Initial pass at writing a polynomial class.
Inefficiently.
"""
class Polynomial_0:
    pass

p1_0 = Polynomial_0()
p2_0 = Polynomial_0()
p1_0.coeffs = 1, 2, 3     # x2 + 2x  3
p2_0.coeffs = 3, 4, 3     # 3x2 + 4x + 3


"""
Better pass at writing a polynomial class.
"""
class Polynomial_1:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

p1_1 = Polynomial_1(1, 2, 3)      # x2 + 2x  3
p2_1 = Polynomial_1(3, 4, 3)      # 3x2 + 4x + 3

"""
Run interactively:
$ python -i data-model.py
>>> p1_0
<__main__.Polynomial_0 instance at 0x107eae2d8>
>>> p1_1
<__main__.Polynomial_1 instance at 0x107eae368>
>>> p2_0
<__main__.Polynomial_0 instance at 0x107eae320>
>>> p2_1
<__main__.Polynomial_1 instance at 0x107eae3b0>
"""

"""
Another enhacement to polynomial class - adding repr around objects.
"""
