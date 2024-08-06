# Modules

- [Modules](#module)
- [Creating Module](#creating-module)
- [Importing Module](#importing-module)
  - [from](#from)
  - [import](#import)
- [Compiled Python Files](#compiled-python-files)
- [Modules Search Path](#modules-search-path)
- [Packages](#packages)

## Module

- Module ni file ambalo lina functionality fulani katika program yako,Ukienda supermarket kuna sehemu mbambali kwa ajili ya product kama, shirts, t-shirts, women clothes.

- Hivyo katika Python kuna modules na pia ni namna yako code zako kuwa organized katika program yako, kwa mfano katika program yako unaweza ukawa na simple function ya kuweza kucalculate cost ya tax pamoja na shipping cost katika program yako.Angalia mfano hapo chini:

```py
# app.py
def calculate_tax():
    pass


def calculate_shipping():
    pass
```

- Hivyo code ambazo zimeandikwa katika program yako zipo katika `app.py` ili ziweze kuwa katika module katika program yako inaweza inabidi kutengeneza file lako lingine likiwa na extension ya `.py` mfano file letu litaitwa `mauzo.py`.

```sh
# create mauzo.py module
touch mauzo.py
```

- Baada ya file lako kutengenezwa inabidi kuhamisha code zako ambazo zipo kwenye `app.py` kwenda kwenye `mauzo.py`, hivyo mauzo.py itakuwa na code zifuatazo ambazo zilikuwa kwenye app.py.

```py
# mauz.py file(module)
def calculate_tax():
    pass


def calculate_shipping():
    pass
```

- Baada ya hapo inabidi

## Creating Module

## Importing Module

- Ili uweze kutumia module katika program yako inabidi kufanya import, kuna namna mbili ya kufanya import katika program yako kwa kutumia `from` na kutumia `import`.

## from

- Namna ya kwanza ya kuimport module utaanza na neno `from` kisha jina la module kisha `import` na hapo utaandika hiyo funcionality yako mfano function ambayo imekuwa defined kwenye program yako.

```py
from mauzo import calculate_tax

calculate_tax()
```

- Pia kama utataka kutumia funcionality ambayo ni zaidi ya moja utatofautisha kwa kutumia mkato.

```py
from mauzo import calculate_tax, calculate_shipping

calculate_tax()
calculate_shipping()
```

## import

- Baada ya module yetu `app.py` kutengenezwa ili uweze kutumia module yako hiyo inabidi kufanya kitu kinaitwa import ambayo ni sawa na kusema kwamba nenda kwenda folder lako kisha tafuta file linaitwa xxx.Angalia mfano wa Sintaksia:

```py
import jina_la_module
```

```py
import mauzo

# imports returns an object
mauzo.calculate_tax()
```

- Kutoka kwenye mfano hapo juu tumefanya import ya module inaitwa mauzo, mauzo inakuwa object ili uweze kutumia functionality zilizopo katika `mauzo.py` inabidi kutumia dot operator., ambapo utaanza na jina module ambayo umeimport ikifuatiwa na dot hapo utaona functions ambazo zipo kwenye module hizo zimekuwa defined kwenye mauzo.py.

## Compiled Python Files

- Baada ya kurun program yako katika file lako kuna file linaitwa `__pyache__`, basi file hilo limekuwa compiled

![Pyache](/assets/pyache.PNG)

## Modules Search Path

## Packages
