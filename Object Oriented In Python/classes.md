# Introduction

## Classes

- Mwanzoni wakati tunaanza kabisa tulitumia built in type inaitwa `type()` kuangalia aina ya data.Mfano:

```py
lugha = "Python"
print(type(lugha)) # <class 'str'>
```

Kutoka kwenye mfano hapo juu tumeangalia ni aina gani ya data ya variable lugha, na jibu ni `<class 'str'>`,katika output hiyo neno inamaanisha kwamba aina ya data ni string `str` ila ni instance ya class,katika Python class inatuwezesha kuweza kuunganisha data pamoja na functionality zake kwa pamoja.

## Objects

- Ili uweze kutengeneza object katika python lazima uwe na class na maana na object ndio inakuja kwamba object ni instance ya class katika Python,na Class ni blueprint ambayo inakuwezesha kuweza kutengeneza object katika Python.Mfano mzuri ni kwa Mnyama(Animal) kutoka kwenye neno Mnyama tunaweza kupata binadamu, simba na wayama wengineo.Hivyo katika programming Mnyama ni mfano mzuri wa class na Binadamu ni mfano mzuri wa object ambayo imetoka katika class ambayo inaitwa Mnyama.

- Katika Python class inakuwa na attributes pamoja na methods(function), Mfano:

```py
lugha = "Python"
```

Variable lugha ni string na kwa kutumia dot operator tunaweza kupata method na function ambazo zipo kwenye string, mfano wa methods hizo ni `capitalize`, `isLower` hizo ni baadhi ya functions ambazo zipo kwenye variable lugha na katika OOP tunaita methods badala ya function.

## Creating Class

- Ili kuweza kutengeneza class katika Python unaanza na `class` ikifuatiwa na jina la class yako, jina la class inabidi liwe katika, pascal naming case.

<details>Pascal naming case
 `Pascal naming case`:Ni namna ya kufanya naming ya variables zako katika programming ambayo kila neno la kwanza linaoanza katika class yako(Upande wa Python) inabidi liwe katika herufi kubwa mfano: Class inaitwa jina la class katika pascal naming litauwa hivi.

```py
class JinaLaClass
```

<summary>
</summary>
</details>

- Mfano tunatengeneza class inaitwa Shape na moja kati ya method katika Hiyo class ni draw kwamba tunaweza kudraw shape kutoka kwenye shape class.

```py
class Shape:
    def draw(self):
        print("draw shape")

```

kutoka kwenye mfano hapo juu kuna class inaitwa `Shape` ikisha na function ambayo ni draw na hiyo function katika object oriented katika Python inabidi iwe na parameter angalau moja na hiyo parameter inaitwa self,mbeleni utaona kwanini tunaweza self parameter.Sasa tumetengeneza class shape je ni kitu gani tunaweza tukafanya na class hiyo.

- Baada ya class kutengenezwa inabidi kutengeneza shape object ambapo tunaita jina la class kama ambayo tulikuwa tunaita function, ila inarudisha shape object hivyo tunaweza tukaipa jina hiyo shape object, tutaita shape.Kwa ile object ambayo imetengenezwa katika program yako utatumia dot operator kuweza kupata methods zilizopo katika class hiyo na mfano wa hiyo method ni `draw()`.

```py
class Shape:
    def draw(self):
        print("draw shape")


shape = Shape()
shape.draw()
```

- Jinsi ambavyo implementation ya class Shape ilivyotengenezwa ikiwa pamoja na function ni sawa na implementation ya class nyingine zinavyofanyika ila kuna utofauti kidogo,Mfano:kutoka kwenye variable lugha `lugha = "Python"` variable lugha inathamani ya `'Python'`, ili kuweza kubadili thamani ya variable kuwa katika herefu ndogo tutatumia `.lower()` method na hiyo method imekuwa implemented kwa kutumia class.

- Katika object oriented kuna function nyingine ambayo inaitwa `isinstance` inatumika kuangalia kama object ni instance ya class au hapana,inachukua parameter mbili ya kwanza ni jina la object yako na ya pili ni jina la class yako.Mfano:

```py
class Shape:
    def draw(self):
        print("draw shape")


shape = Shape()
shape.draw()

print(isinstance(shape, Shape)) # True
```

## Constructors

- Constructor ni special function katika OOP ambayo inatengenezwa pale ambapo tunatengeneza new shape object,ili kuweza kutengeneza constructor tunatengeneza special function,Mfano:

```py
# working with classes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def Drive(self):
        print("Driving.")

# creating a Car object
car = Car("Toyota", "Cruiser", 2024)
car.Drive()
```

- Constructor ni method ambayo ni malumu ambayo inatumika kufanya initialization ya objects ambazo zinakuwa defined kwa kutumia `__init__` method ndani ya class.Kutoka kwenye mfano pale juu sehemu ya init ili kuweza kutengeneza hiyo special method kwa kutumia `__init__` ni function utaanza na def keyword ikiwakilisha function kisha hiyo fucntion ina default parameter ambayo ni self.kisha ndani yake utaweka majina ya attributes zako katika program yako na hizo attributes huwa ni variables, baada ya self parameter weka majina ya variable ambazo kwenye progam yetu kuna `make`, `model` na `year`, baada ya kufanya hivyo inabidi hizo attributes tukabidhi kwa hiyo self parameter ili zikiwa called automatically inakuwa na hizo arguments.

- Hivyo ndani ya hiyo object hizo attributes zinaweza kuwa na default values au unaweza ukawa sawa na jina la variable.Mfano hapo chini tunafanya namna tunaweza tukawa na attribute ambayo ina default value mfano ni `self.year`, ila sio lazima na kama value yako haina default unaweza ukawa sawa na mfano wa chini kabisa `self.year = year`

```py
# working with classes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = 2024

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = 2024
```

- Pale ambapo new car object inatengenezwa `__init__` method inaitwa automatically ikiwa na arguments zake, kumbuka `self` ni reference kwenda kwenye part object.

## Class Attributes Vs Instance Attributes

- Class level attributes, vipi kama tunataka kutengeneza attribute ya car object ambayo ni sawa kwenye upande waote yani kwamba haibadiliki, Mfano: Binadamu wote tuna macho mawili, sasa kwenye car object labda nataka kubadili kwamba car object iko na default style ambayo ni `german` style ila kwenye car object ambayo ni instance ya `Car` class.

- Inabidi kufanya declaration ya default_style attribute ya car object ila ndani ya Car class.

```py
class Car:
    default_style = "German Style"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
```

- Hivyo default_style ni class level attribute ambayo tunaweza tukaisoma kupitia class reference au object reference.Kumbuka kwamba class attributes zinakuwa shared katika instance zoe za class na unaweza kubadili class level attribute,Mfano:

```py
# working with classes
class Car:
    default_style = "German Style."

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def Drive(self):
        print("Driving.")

# creating a Car object
car = Car("Toyota", "Cruiser", 2024)
print("Default value: ", car.default_style)

# changing class attribute value
car.default_style = "Japanese Style."
print("Changed value: ", car.default_style)
```

## Class Methods vs Instance Methods

- Kuna class methods na instance methods, instance methods ni zile method ambazo zinakuwa called pale ambapo instance object inakuwa initialized katika class yako.Mfano:Kutoka kwenye mfano hapo juu kuna method mbili ambazo ni instance za car object,na pia instance methods zinakuwa called ambapo instance object inakuwa initialized katika program yakoMfano wa instance method ni `Drive` ambayo inakuwa initialized pale ambapo car object inakuwa created kutoka kwenye `Car` class. Na special method `__init__` pia ni instance ya class object.

```py
# working with classes
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def Drive(self):
        print("Driving.")

# creating a Car object
car = Car("Toyota", "Cruiser", 2024)

```

- Class method ni function ambayo ipo kwenye class level ya class yako ila sio instance ya class object kwa sababu haiwezi kuwa called hadi instance object inakuwa initialized kwenye program yako,mfano tunatengeneza class method ambayo inaitwa `sound`, tunaanza na jina la class kisha tunatumia dot operator kuweka hiyo method ya class, baada ya hapo tunahifadhi hiyo method ya Car class ndani ya car object. MfanO;

```py
car = Car.sound()
```

- Baada ya hapo inabidi hiyo function iwe defined kwenye class level value, tunaanza na def keywotrd kisha jina la function ila parameter ambayo inachukuliwa na `cls` ambayo ndio reference kwenye class.Ila baada ya kufanya definition hiyo cls object ni method na tunaweza kuweka baadhi ya value ila kwenye program yetu hakuna value ambayo tunaweka hiyo tutarudisha cls method bila parameter yoyote.Ila juu ya function yako kuna kitu ambacho ni muhimu sana kinaitwa decorator, ili tuweze kuifanya class kuwa na class method sound inabidi kutumia decorator ambayo inaitwa `@classmethod` kwa ajili ya kufanya decoration,Angalia mfano vizuri hapo chini!

```py
# working with classes
def drive():
    print("Driving.")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @classmethod
    def sound(cls):
        return cls('make', 'Toyota', 2023)


car = Car('make', 'Toyota', 2024)

```


## Magic Methods

- Ni zile method ambazo zina underscore mbili mwanzoni na mwishoni,Magic methods zinakuwa called automatically na Python interpreter ila inatengemeanana namna ambavyo tunatumia object na class.Mfano wa magic methods 

```py
__init__, __str__, __annotations__, __delattr__, __dict__, __eq__, __format__, __getattribute__, __getstate__
```

- Zipo nyingi ila hizo ni baadhi ya,Mfano: __init__ tumetumia wakati wa kufanya definition ya attributes katika class yako ila pia inakuwa called automatic pale ambapo instance ya object inakuwa inatengenezwa kutoka kwenye class,Mfano:

```py
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


# init called automatically
car = Car('make', 'Toyota', 2024)
```

- Section inayofuata [Comparing Objects.](/Object%20Oriented%20In%20Python/comparing%20objects.md)