<!--

 Translate explanations of variables, data types (e.g., integers, floats, strings, lists, dictionaries), and variable naming conventions.

Include examples of declaring variables and performing operations on different data types 

-->

# Variables

- [Introduction](#introduction)
- [Data Types](#data-types)
  - [Booleans](#booleans)
  - [Float](#floats)
  - [Numbers](#numbers)
  - [String](#string)
- [built in type](#built-in-type)

## Introduction

- Variable: Ni container ambalo linahifadhi taarifa(data au information) katika memory ya computer.Variable ndio msingi wa taarifa katika computer, ni kama ambavyo watu tunamajina kwamba ukiita jina la mtu fulani anajua kwamba yeye ndio kaitwa na pia akiitwa mtu mwingine anajua kwamba sio yeye aliyeitwa.

- Ili kuweza kutengeneza variable katika Python lazima variable yako iwe na jina na pia thamani(values), mfano: tunatengeneza variable ambayo inaitwa miaka ambayo inahifadhi miaka ya mtu katika memory ya computer, tunaanza na jina la variable yako na thamani yake.

```py
miaka = 30
```

- Wakati computer inaangalia variable yako itafanya allocation ya memory kwa ajili ya program yako,iko hivi baada ya computer kuona variable yako itabidi kuangalia taarifa gazi zinahifadhiwa na kisha itahifadhi katika memory yake.Na pia ni kama una box linaitwa miaka na ndani yake linathamani ya 30 hivyo katika memory variable name ni kama label ya memory location ya variable.Ili kuweza kuona thamani ya variable yako katika terminal tunatumia `print()` function, print function ni built-in function kwamba ipo humo humo na ina uwezo wa kutumika katika program kuweza kupata output kwenye screen.Unaanza na print function na mabano na ndani yake unapitisha jina la variable yako.

```py
miaka = 30
print(miaka)
# Jibu: 30
```

## Data Types

- Je ni aina gani ya data ambazo tunaweza tukahifadhi katika memory ya computer? Kuna aina mbalimbali ya data ambazo tunaweza tukahifadhi katika memory ya computer.Kuna build-in types ambazo ni primitive.Kuna aina 3 za primitive type katika Python ambazo ni namba, bulliani(booleans) na tungo(string).Kwenye upande wa namba kuna aina mbili ambazo ni integer pamoja na float.

## Booleans

- Bulliabi inatumika kuhifadhi taarifa ambazo ni `kweli` au `sikweli`, na pia ni muhimu majina ya variable zako inabidi yawe katika mtindo wa kivumishi, kujua zaidi kuhusu variable naming conventions hakikisha unapitia [hapa.](/basics/best_practices.md)

- Hivyo majina ya variables zako inabidi yawe katika kivumishi(ajectives), kwamba ukivumisha kitu katika program yako kinaweza kuwa kweli au sikweli na pia kwenye upande wa English majina ya variables zako inabidi yawe katika hivyo pia ni moja kati ya best practices.Majina ya variable yanabidi yawe vizuri kwamba muda mwingine mtu akisoma msimbo wangu anajua umefanya kti gani na kwanini umefanya hivyo.Mfano wa bulliani:

```py
mrefu = True
amesajiliwa = False
amepiga_kura = True
```

- Kuangalia kama data type yake ni bulliani tunatumia built-in function `type()` na parameter ambayo tunapitisha ni jina la variable yako.Mfano:

```py
amesajiliwa = False
print(type(amesajiliwa)) # Output: <class 'bool'>
```

## Floats

- Float ni aina ya taarifa ambazo zipo katika mfumo wa desimali,Hivyo interpreter ya Python ikiona taarifa ipo katika desimali inajua kwamba hii data ni float na kama ni namba kamili inajua kwamba hii data ni namba kamili, kuna built-in function ambayo inaitwa `type()` ndani yake unapitisha jina la variable yako na yenyewe itarudisha aina ya data yako.Ili kuweza kufanya intialization ya variable yako utaanza na jina la variable ikifuatiwa na = na pia thamani yake ambayo ni thamani iliyo na desimali.Mfano:

```py
interest_rate = 12.4
```

## Numbers

- Namba ni aina ya taarifa ambazo zinahifadhiwa katika computer ambazo zipo katika tarakimu.Kwenye upande wa namba kuna aina mbili ambazo ni integer pamoja na float katika Python. Integer ni taarifa ambazo zinahifadhiwa katika memory ambazo ni namba kamili bila desimali, mfano: miaka ya mtu, idadi ya watu na kadhalika.Ili kuweza kufanya intialization ya variable yako utaanza na jina la variable ikifuatiwa na = na pia thamani yake ambayo ni namba kamili.Mfano:

```py
miaka = 30
idadi_ya_wanafunzi = 45
```

## String

- String inawakilisha tungo au sentensi katika kiswahili, kwenye upande wa tungo,Tungo zinatumika kwa ajili ya kuhifadhi data za majina ya watu katika Python, kitu chochote ambacho kipo katika tungo au sentensi ndio tunaita string.Mfano wa string katika Python ni jina la mtu, jina la mnyama na kdhalika.Kufanya initialization ya string katika Python unaanza na jina la tungo yake ikifuatiwa na = kisha double quotes au single quotes.Mfano:

```py
jina = "Godbless Nyagawa"
mnyama = 'Simba'
```

- Ni muhimu kujua kwamba ni muda gani inabidi kutumia double quotes na single quotes, kwa mfano kama katika sentensi yako au string yako kuna neno ambalo lina single quotes ndani yake basi inabidi kutumia double quotes kwa ajili ya program yako.Ila kama ndani yake kuna double quotes basi ndani inabidi kutumia single quotes.

```py

```

- Tungo ina builtin data type yake ambayo ipo kwenye Python ambayo inatumika kufanya initialization ya variable katika program yako.`str()` function inachukua string ambayo ipo kwenye single quotes au double quotes na kisha kuifanya kama variable: str inachukua string kama paramter, mbeleni tuajifunza je parameter ni nini na pia zinafanya kazi kivipi. Mfano:

```py
jina = str("Godbless Nyagawa.")
print(jina) # Output: Godbless Nyagawa.
print(type(jina)) # Output: <class 'str'>
```

- Kwenye mfano hapo juu tumetumia str() built in function kufanya initialization ya string na kisha tumeangalia aina ya taarifa na jibu lake ni str yaani string.

- Vipi katika unataka kuprint output ambayo ni string ila ni text ndefu, basi hapa tunatumia triple qoutes `""""""`.Mfano:

```py
meseji = """
Habari! Karibu

Ujifunze Python kwa kutumia lugha ya kiswahili, Ni rahisi

Ahsante.
"""
```

## built in type

- Katika Python kuna built in function `type()` inatumika kuangalia aina ya data ambao variable yako imechukua, inachukua parameter ambayo ni aina ya variable.

```py
amesajiliwa = True
name = "Godbless Nyagawa"
miaka = 30
interest_rate = 5.7

print(type(amesajiliwa)) # <class 'bool'>
print(type(name)) # <class 'str'>
print(type(miaka)) # <class 'int'>
print(type(interest_rate)) # <class 'float'>
print(type(print)) # <class 'builtin_function_or_method'>
```

- Kama ambavyo unaona kwenye mfano hapo juu hata ukijaribu kuangalia aina ya taarifa ya built in function inakwambia kwamba ni built in function au method.
