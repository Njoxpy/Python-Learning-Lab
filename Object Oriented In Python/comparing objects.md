# Objects

## Comparing Objects

- Katika Python tunaweza kufanya comparison ya object moja na yingine ambayo ni instance ya class.Mfano:

```py
# working with classes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car("Cumy", "Toyota", 2023)
another_car = Car("Cumy", "Toyota", 2023)

print(car == another_car) # False
```

- Kutoka kwenye mfano hapo juu tumefanya comparison ya object `car` na object `another_car` ambazo zote ni instance ya class `Car`,Jibu ni false kwanini? Katika Python hata pia JavaScript unapofanya comparison ya object moja na object nyingine kinachofanyika pale ni comparison ya reference(address) ya object moja nyingine katika Memory, hivyo haiwezekani kuwa na object mbili ambazo zote zina same memory location ndio maana unapata false.Hivyo tumefanya comparison ya memory location na sio value.Ili kuweza kufanya comparison tuatumia magic method `__eq__` ambayo itakuwa called pale ambapo tutafanya comparison ya objects.

## eq Magical Method

- Mwanzoni sehemu ya magic method nilisema ni zile method ambazo zipo katika Python zinaanza underscore mbili.Hivyo ili kufanya comparison ya object moja na nyingine tutatumia `__eq__` method, itakuwa called automatic pale ambapo object inakuwa compared.

```py
# working with classes
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __eq__(self, other):
        return self.model == other.model and self.year == other.year


car = Car("Toyota", 2023)
another_car = Car("Toyota", 2023)

print(car == another_car) # True
```

- Kwenye mfano hapo juu ili kuweza kufanya comparison ya object moja nayingine tumefanya defintion ya magic method `__eq__` na inachukua parameter mbili ya kwanza self na ya pili ni object nyingine ila kama best practice tumia `other` ikimaanisha other object ila ndani ya hiyo magic method kwenye body tunarudisha value baada ya kufaya comparison ya attribute value ya attributes ambazo `model` na `year`, ila chini tunacreate new instance object ila kumbuka kwamba kwamba magic method inakuwa called pale ambapo object inakuwa called.
