# python package index

## Introduction

- Python Package index, ni kama `npm` kwa wale ambao wametoka kwenye upande wa web development,unatumia pi kwa ajili ya kusanikisha(installation) program, kufanya upgrade pamoja kutoa package kwa kutumia program inaitwa `pip`, pip unakuwezesha kuweza kusakinisha packages kutoka kwenye Python package index kwa kifupi inaitwa PI.

## pip

- Ili kuweza kufanya installation ya package katika python tutatumia command inaitwa pip.Mfano ili kuweza kufanya installation ya package kwa kutumia pip tunaanza na neno pip kisha neno install na jina la package.

```python
# installing package using Python
pip install packageName

# installing requests
pip install requests
```

- Upgrading package,ili kuweza kufanya upgrade ya package katika python kwa kutumia pip itakuwa hivi.

```python
pip install --upgrade pip
```

- Kuweza kuona list ya package ambazo zimekuwa installed katika Python utaanza na jina la package kisha neno list, itarudisha list ya package zote ambazo zimekuwa installed kwa kutumia Pip.

```python
# lists all packages
pip list
```

- Ili kuweza kuona idadi ya command zote ambazo zinatumika kwa kutumia pip katika program yako tumia pi help.

```python
pip help
```

- Ili kuweza kufanya installation ya version fulani kwa ajili ya program inabidi kuongeza `===` kisha version, major vesrion, minor version na patch(bug fixes).

```py
pip install requests=2.9.0
```

- Kama unataka kufanya installation ya version ambayo iko na patch ambayo imekuwa fixed katika program yako tutatumia `*` hiyo itafanya installation ya (latest)standard version katika program yako.

```py
pip install requests=2.9.*
```

## Virtual Environments

- Virtual environment inatusaidia ili kuweza kufanya installation ya package ambazo unaweza ukatumia katika program zako,Mfano unaweza ukawa na package moja na version tofauti ambayo unaweza ukatumia kwa ajili ya shughuli mbalimbali.Ili kuweza kutengeneza virtual environment katika python inabidi kutengeneza hiyo virtual envrinment katika program yako.

```py
python -m venv folderName
```

- Baada ya kufanya installation ya program yako katika programu hiyo inabidi kufanya activation ya hiyo virtual environment.

```py
scripts/activate.bat
```
