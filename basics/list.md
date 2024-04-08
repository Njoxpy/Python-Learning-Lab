# List

## Introduction

- List inatumika kuhifadhi group za item, mfano majina ya wanafunzi, marks za wanafunzi.Kufanya declaration ya list unaanza na [] mabano mraba na ndani yake unaweka items zako.Unaweza ukawa na list ya numbers, list ya tungo(string), list ya bulliani(boolean), pia unaweza ukawa na list ya list.Item moja na nyingine katika list yako inatofautishwa na mkato `,`.Mfano:

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

maksi_za_wanafunzi = [87, 86, 80, 89]

bulliani = [True, False, True, False]

maksi = [12, 15, [13, 14], 34, [14, 15]]
```

- Kutoka kwenye mfano hapo juu kuna list ya majina ya wanafunz ambayo ipo kwenye string, list ya maksi ya wanafunzi ambazo ziko katika namba, list ya thamani ya bulliani, list ya maksi ya wanafunzi ambazo ndani ya list kuna list.

- Hivyo ndio namna list zinakuwa declared katika Python ila kuna namna nyingine ya kufanya declaration ya list katika program yako,Mfano unataka kufanya declaration ya list ya namba kumi ila inabidi ziwe 30 yaani namba 10 ziwe 30 katika list yako.

```py
kumi = [10] * 30
print(kumi)
```

- Kutoka kwenye mfano hapoo juu tumefanya declaration ya list kumi ikiwa na value 10 ila zipo 30 kwenye list kumi.Kufahamu zaidi kuhusu list katika Python hakikisha una hakikisha una Python interactive environment, au tumia search button kisha andika `python` au unaweza nenda kwenye CMD au andika Python kisha utakutana kitu kama hichi.

![Python Interactive Environment](/assets/Python%20Interactive%20Environment%20list.PNG).

- Andika neno `help()` kisha andika data type ambayo unatafuta ila kwetu tunatafuta list hivyo andika list, kisha utakutakana na taarifa zote kuhusu list namna zinafanya kazi.

## list built-in

- Katika Python kuna built-in function ambayo inaitwa `list()` inachukua argument kama hakutakuwa na ragument katika program yako itarudisha list ya item ambayo ni empty.

```py
lst = list()
print(lst)  # Output: []
```

- kwenye mfano hapo juu, declaration ya lits imefanyika kwa kutumia `list()` built function na baada ya kupata output yake ni empty kwa sababu, list ipo empty hakuna argument iliyo pitishwa katika list yako.Unaweza kutengeneza list ya items ambazo zipo katika characters.

```py
lst = list("Sema Dunia!")
print(lst)  
# Output: ['S', 'e', 'm', 'a', ' ', 'D', 'u', 'n', 'i', 'a', '!']
```

- Declaration ya list imefanyika na ndani ya list function tumepitisha string ambayo ni list kwamba kila element katika program yako inachukua element moja.

- Unaweza pia kutengeneza list ya items ambazo zipo katika range fulani labda kuanzia 1 hadi 10, unatrumia list built in function na ndani yake unapitisha range function.Ila counting inaanzia sifuri na namba ya mwisho inakuwa ignored.

```py
numbers = list(range(10))
print(numbers)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## length of the string

- Kupata length ya string yako, tunatumia `len()` function, na len function inarudisha idadi ya items ambazo zipo kwenye list yako.Mfano

```py
lst = list("Sema Dunia!")
print(len(lst))
```

- Kupitia len function tunaweza kutengeneza simple project ambayo tutatumia kuangalia kama password imezidi herefu 6 au hapana.

```py
# uliza jina la mtumiaji
name = input("Jaza username yako: ")
passowrd = input("Jaza password yako: ")

if len(passowrd) > 6:
    print("Karibu!")
else:
    print("Password haiwezi kuna na herufi ambazo ni chini ya 6")
```

## Accessing Items in A list

- Kitendo cha kupata access ya items katiak list yako tunaita index, kwenye upande wa Python kuna namna mbakimbali ambazo unaweza ukapata access ya element fulani katika list yako.

- Kupata access ya element katika list yako tunatumia square brackets na ndani yake tunawezaka namba ya element ambayo unataka kupata access yake ila kumbuka kwamba items katika list zinahesabiwa kuanzia 0 na kuendelea, hivyo element ya kwanza inakuwa katika index ya sifuri.

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

print(majina_ya_wanafunzi[0]) # returns the first element in the list
```

- Kupata index ya element ya kwanza kutoka mwisho katika list:

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']
print(majina_ya_wanafunzi[-1])
```

## Modifying items By indexing

- Kufanya modification ya item yako ambayo ipo katika list lazima ujue index ya element yako kisha kufanya assignment ya value mpya ya element yako.

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

majina_ya_wanafunzi[0] = "Simo Kimbangu"

print(majina_ya_wanafunzi)
```

## Slicing

- Vipi kama unataka kupata index ya element katika list yako kuanzia element fulani katika list hadi element fulani katika program yako kwamba range fulani basi hapa ndio tunatumia slicing.Mfano kutoka katika list `majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']` utaanza na jina la list yako na square brackets na kisha ndani yake, unaweka range ambayo unatka element zako ziwe sliced, Mfano:

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

print(majina_ya_wanafunzi[0:3])
```

kutoka kwenye mfano hapo juu tumepata access ya element kuanzia index ya 0 hadi 3 ila katika Python index ya kwanza inakuwa included ila index ya pili inakuwa excluded ndio maana strign "Ronald Chaula" imekuwa excluded, pia ni muhimu kuzingatia kwamba slicing haibadili original array yenyewe inatengeneza copy ya array.

- Kupata indexing ya element ya array kwa range: mfano list ambayo ina namba kuanzia 0 hadi 20 ila unataka kupata element ambayo ni shufwa kwa kutumia indexing.

```py
lst = list(range(21))
print(lst[::2])
```

- Kupata element(namba shufwa) za list ila ziwe katika reversed order.

```py
lst = list(range(21))
print(lst[::-2])
```

## List Unpacking

- Kama tunataka kupata individual elements katika list kisha kustore katika variable yako,mfano una list ambayo inaitwa number ikiwa na variable yake.Kitendo hicho kinaitwa unpacking kwamba kwa kila variable ambayo tumefanya declaration kwenye program itachukua variable moja katika list yako

```py
numbers = [1, 2, 3, 4]
first, second, third, fourth = numbers
```

Tunatengeneza separate variable kutokana na idadi ya elements katika list, kila variable itachukua index ya element ambayo ipo kwenye array.

- Vipi kama idadi ya list ni nyingi ila unataka kuchukua baadhi ya element katika list yako, tunafanya unpacking kwa first element na second element katika program yako, kisha kwa element ambazo hauhitaji kuanyia unapcking unaanza na nyota(* asterisk) na jina la variable.Mfano:

```py
lst = list(range(21))
first, second, third, fourth, *others = lst
```

## Looping Over List

- Je kufanya iterating kwenye loop katika list unafanyaje? Unatumia for loop.Unaanza na neno for kisha jina la variable ambalo litashikilia kila variable kwa kila iteration ya list na kisha in keyword ikifuatiwa na jina list.

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

for mwanafunzi in majina_ya_wanafunzi:
    print(mwanafunzi)
```

- Ili kuweza kupata index ya hiyo element pamoja na variable katika list yako inabidi kutumia `enumerate` object enumerate object inarudisha tuple ikiwa na index ya element pamoja na element yako.

```py
majina_ya_wanafunzi = ['Godbless Nyagawa', 'Elvis Mathew', 'Neicore Adam', 'Ronald Chaula']

for mwanafunzi in enumerate(majina_ya_wanafunzi):
    print(mwanafunzi)
```

## 