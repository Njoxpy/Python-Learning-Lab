# Aithmetic

- Vipi kama tunataka kufanya operation katika object yako,ila kwa hapa nitatumia mfano mwingine

```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(12, 13)
another_point = Point(23, 12)
```

- Kwa mfano kutoka kwenye mfano hapo juu tuna Point Class ambayo ina instance ikiwa na attributes x na y, ila ukijaribu kufanya arithmetic operation ya value ya x ya object `point` na `another_point` object itakuwa hivi.

```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(12, 13)
another_point = Point(23, 12)

print(another_point + point)

"""
TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
"""
```

- TypeError; kwamba hio operesheni haiwezekani kwahiyo badala ya kufanya hivyo tuatumia magic methods kuweza kufanya operation ya instance ya object point na another_point x instances.

```py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x


point = Point(12, 13)
another_point = Point(23, 12)
```
