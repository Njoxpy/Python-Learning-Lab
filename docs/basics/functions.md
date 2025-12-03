# Functions

- [Introduction](#introduction)
- [Arguments](#arguments)
- [Types Of Function](#types-of-function)
- [Default Argument Values](#default-argument-values)
- [xargs](#xargs)
- [xxargs](#xxargs)
- [Scope](#scope)
- [Best Practices](#best-practices)

## Introduction

- Katika function mwanzoni kabisa umekutakana na built-in function, kama `print()`, `input()`, `round()` na nyinginezo, sasa unaweza pia kutengeneza function yako mwenyewe kwa kutumia llugha ya python kama ilivyo kwenye lugha nyingine kama JavaScript.

- Kutengeneza function katika Python unaanza na neno `def` ikimaanisha define na kisha jina la function yako na mabano kisha `:` na ndani ya hiyo function unaweza msimbo wako kutokana na jina la function yako.

```py
def toa_salamu():
    print("Habari")
```

- Kutoka kwenye mfano hapo juu tumetengeneza function inaitwa toa_salamu ambayo ndani yake(function body) kuna msimbo print("Habari), ukijaribu kutekeleza(run) code yako haitafanya kitu chochote.

- Ilin function yako iweze kutekeleza na kuleta majibu inabidi kuita function yako(call a function), kwa kuandiika jina la function yako chini baada ya kuitengeneza na pia ni muhimu kuacha nafasi mbili kabla ya kuita function yako baada ya function declaration.

```py
def toa_salamu():
    print("Habari")
    
    
toa_salamu()
# Output: Habari
```

-

## Arguments

- Ukiangalia built-in function kama `print()` zinachukua input mfano:

```py
print("Najifunza function")
# Najifunza function
```

- Kutoka kwenye mfano hapo juu function ambayo built-in print inachukua input ambayo ni `"Najifunza function"` je ni kw namna gani tunaweza kutengeneza function yetu ya toa salamu iweze kuchukua input pia? Baada ya jina la function yako ambayo ni `toa_salamu()` ndani ya mabano huwa tunawezaka parameter sawa ambavyo kwenye print function tunaweza tukaweza string, number au float. Ila kwenye function itakuwa na parameter ambayo ni jina, kwamba baada ya kuweka function yetu tutakuwa na output ya `"Habari" + jina la mtumiaji`.

```py
def toa_salamu(jina):
    print(f"Habari {jina}.")
    
    
toa_salamu("Elvis");
# Output: Habari Elvis
```

- Kutoka kwenye mfano hapo juu tumeweka parameter ambayo inaitwa jina na mda wa kuita function inabidi kupitisha hiyo value ila kwenye programming way inaitwa argument.Function inaweza ikawa na parameter zaidi ya moja.

- Kuna utofauti katia ya parameter na rgument parameter ni jina la variable na argument ni value ya variable yako, hivyo unaweza ukawa na parameter inaitwa miaka ikawa na value ya 20.

- Function yako unaweza ukatumia sehemu zaidi ya moja, kitu kinachohitajika ni jina la function yako na value yake.

```py
def toa_salamu(jina):
    print(f"Habari {jina}.")
    
    
toa_salamu("Elvis")
toa_salamu("Njox")
```

## Types Of Function

- Kuna aina mbili za function katika programming.

1: __Function ambazo zina performa task__: Ni zile function ambazo zinasaidia kwa ajili ya kufanya task fulani bila kuwa na return statement katika program yako.

```py
def toa_salamu(jina):
    print(f"Habari {jina}.")
    
    
toa_salamu("Elvis")

```

2: ___Function ambayo inarudisha value__: Ni ile aina ya function ambayo inarudisha return statement fulani katika program yako.

```py
def toa_salamu(jina):
    return f"Habari {jina}."
    
    
messeji = toa_salamu("Elvis")
print(messeji)
```

## Default Argument Values

## xargs

- Function ambayo inachukua kiasi kingi cha ragument kutokana na requirements zako,na number of arguments ni infinite katika program yako ila, katika parameter inakuwa prefixed na nyota(asterisk). Mfano:

- Vipi kama unataka kutengeneza function akatika program yako ambayo inachukua ianzidisha namba kwenye program yako, Mfano:

```py
def zidisha(x, y):
    return x * y
    

jibu = zidisha(12,13)
print(f"Jibu ni {jibu}")
```

- Kutoka kwenye mfano hapo juu kuna function zidisha ambayo inachukua namba x na y kama parameter katika program yako, ila vipi kama tutaongeneza argument moja kama namba 15 katika zidisha function, italeta error kwa sababu zidisha function inachukua parameter mbili ila baada ya kuangalia itakuta kwamba kuna arguments nyingi zaidi ya idadi ya parameter ambayo zinapitishwa.Mfano:

```py
def zidisha(x, y):
    return x * y
    

jibu = zidisha(12,13, 13)
print(f"Jibu ni {jibu}")
"""
    jibu = zidisha(12,13, 13)
           ^^^^^^^^^^^^^^^^^^
TypeError: zidisha() takes 2 positional arguments but 3 were given
"""
```

- Imeleta error sasa kuweza kusolve hilo tatizo itabidi kureplace parameter x na y kwa parameter moja katika program yako ila jina la parameter inabidi liwe katika wingi(ikimaanisha kwamba ni collection ya arguments katika program yako), ila hiyo parameter yako inakuwa prefixed na nyota (*), Mfano:

```py
def zidisha(*numbers):
    print(numbers)  
    

zidisha(12,13, 13) # Output: (12, 13, 13)
```

- Kwenye mfano hapo juu kuna function ambayo ni zidisha na pia inachukua parameter *number ambayo ni infinite, sasa ndani ya function yetu tumejaribu kuprint numbers tumepata 12, 13, 13 kwanini hizo ni list za items ambazo zipo kwenye mabano ila kumbuka list ya items ambazo ziko kwenye mabanao zinaitwa tuples hiyo tunaweza kufanya looping pia katika hizo list kwenye program yetu.

```py
def zidisha(*numbers):
    for number in numbers:
        print(number)
    

zidisha(12,13, 13)
```

- Tumnepata list ya items(tuples) ambazo ni arguments zimepitishwa kwenye program yetu.Hivyo kitu chochote ambacho tunaweza kuafanya na list pia hapa tunaweza kwa sababu ni list items, unaweza kuangalia namba kubwa, kutafuta total na pia kuangalia duplicates.

## xxargs

- xxargs ni tofauti na xargs kwa sababu args inachukua nyota moja ila xxargs inachukua nyota mbili na output ya xxargs ni key value pair ambayo ni dictionary.Pale ambapo unatumia ** unaweza kupitisha key value pairs kama arguments na Python itapitisha kwenda katika mfano wa dictionary.

```py
def save_user(**user):
    print(user) # Output: {'jina': 'Godbless Nyagawa', 'miaka': 12, 'course': 'Computer Science'}


save_user(jina="Godbless Nyagawa", miaka=12, course="Computer Science")
```

- xxargs ndio namna ambavyo dictionary inafanya kazi, arguments zinazopitishwa kwenye function ni keyword arguments.

## Scope

- Scope ni region ya code ambayo variable inakuwa defined.

- Scope katika Python ni sawa na kwenye JavaScript na lugha nyingine, kuna aina mbili za scope: `Local scope` na `global scope`, kila moja ina maana yake na visibility yake katika program yako.

- Local scope ni ile scope ambayo ipo local kwa program yake au naweza nikasema kwamba wigo wake ni local kwenye program yako, variable ambazo zipo katika local scope katika program yako zinaitwa local variable.Angalia mfano:

```py
def greet_user(name):
    print(f"Habari {name}!")
    
greet_user("Njox")
```

Kutoka kwenye mfano hapo juu tumefanya definition ya function inaitwa `greet_user()` ambayo inachukua jina kama parameter na variable name ni local variable kwa sababau unaweza kupata access ya hiyo variable ukiwa ndani ya hiyo function tu na sio nje, Je nini kitatokea endapo tukajaribu kupata access ya hiyo variable nje ya hiyo program.

```py
def greet_user(name):
    print(f"Habari {name}!")
    
greet_user("Njox")

print(name)

"""
Habari Njox!
Traceback (most recent call last):
  File "c:\Users\Njox\Desktop\30 days of python\day 3\app.py", line 16, in <module>
    print(name)
          ^^^^
NameError: name 'name' is not defined
"""
```

- Tumepata error kwamba `name is not defined` kwa sababu name variable ipo nje ya scope kwenye program yetu hii inasababishwa kwa sababu name ipo local kwa hiyo function.Kama umetoka kwenye upande wa C++ kuna kitu kinaitwa memory management na kuna aina tatu za memory management automatic, static na dynamic ila kwenye Python hauhitaji kujua kuhusu memory management kwa sababu yote haya yanafanywa na interpreter kwenye program yako hivyo kwenye  Python pale ambapo umefa nya declaration ya vraibale yako ambayo ni local variable memory inakuwa allocated ila baada ya kuita function yako na kufanya operation katika function yako memory inakuwa freed(deallocated) kwa sababu ni local variable,hivyo local variable inakuwa katika stack ila kwenye upande wa global variable ni tofauti.

- Global scope ni ile scope ambayo ipo global kwamba unaweza kupata access ya variable ukiwa katika sehemu yoyote katika program yako tofauti na local variable.Unaweza kupata access ya variable yako ambayo imekuwa declared kwenye line ya kwanza 1 ila ukajaribu kupata access yake ila wewe upo kwenye line ya 20.Mfano:

```py
jina = "Godbless Nyagawa."

def greet_user(jina):
    print(f"Karibu {jina}.")
    

greet_user("Njox") # Output: Karibu Njox.

print(jina) # Output: Godbless Nyagawa.
```

- Kutoka kwenye mfano hapo juu, jina ni global variable ila kwenye function kuna variable nyingine jina ambayo ni local variable ipo local kwenye function yako kumbuka kwamba global variable ni global inaweza kuwa accessed sehemu yoyote kwenye program yako. Declration ya global variable ni lifetime kwamba ikiwa declared kwenye program yako itakaa pale hadi pale ambapo utafuta kwenye program yako na pia ni muhimu kuzingatia kwamba global variable inachukua nafasi kubwa katika memory, hakikisha program yako inagawanywa katika function ili iweze kuwa na local variables kwa sababu ni effficient.

## Best Practices

- Hakikisha jina la function liwe meaningfull na descriptive.

- Hakikisha majina ya function zako zipo katika herufi ndogo.

- Tumia underscore kutofautisha neno moja na lingine kwenye function yako.

- Hakikisha mwili wa function ya msimbo wako upo katika indentation husika inayotakiwa kwenye program yako.

- Penda kutumia local variables katika program yako badala ya global variables katika program yako.
