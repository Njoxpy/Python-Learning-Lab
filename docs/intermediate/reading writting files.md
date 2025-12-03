## Reading and Writting Files

- Katika Python tuna uwezo pia wa kuweza kusoma na kuandika katika faili za computer yako.

- Ili kuweza kuifanya hizi operation zote katika Python tunatumia file object ili kuweza kusoma na pia kujua content zilizopo kwenye file lako, mfano unaweza ukawa unatumia kwa ajili ya kuangalia ni vitu gani vipo ndani ya file za `file.,txt` au file lingine ambalo unataka kufanyia manipulation fulani.

- Kwa kutumia `open` object katika Python kwa kuanza na neno open inarudisha file object na pia file object inachukua parameter tatu ambazo 2 ni `postional arguments` na moja ni `keyword argument`.argument ya kwanza ni string am,bayo ni jina la file na inabidi liwe katika string na argument ya pili ni mode yaani operation ambayo unataka kufanya katika file lako, kuna mode 4 ambayo ya kwanza ni `w` ikimaanisha write kwamba unatakla kuandika kwenye file, mode ya pili ni `r` ikimaanisha read kwamba unataka kusoma kitu fulani katika program yako, mode nyingine ni`a` ikimaanisha append ,append inachofanya ni kwamba kama tayari kutakuwa na content katika file basi yenyewe itakachofanya ni kuweza kuongezea pia kufuta vitu vilivyopo.

- Mode nyingine ni `b` ambayo inafungua file lako katika binary mode, na argument ya mwisho ni keyword argument, mara nyingi file huwa zinafungulia zikiwa katika text mode, hivyo inabidi kuwe na ecndoing ya program yako na moja kati ya encoding inayotumika ni `utf-8` hivyo itakuwa hivi. `encoding="utf-8"`, ngoja tuangalia kwa ujumla inafanyika vipi kwenye program yako.

```py
# fungua file katika mode ya kuandika,kisha tunahifdhi katika object f
f = open ("file.txt", 'w', encoding="utf-8")

# tumia f object ambayo inamethod ya write na ndani yake unaandika kitu ambacho unataka kuandika
f.write("hello, najfunza reading and writting files!")

# funga file baada ya kumaliza kuandiuka
f.close()
```

- Kuna namna hiyo ya kuweza kuandika pia kuweza katika file lako ni njia nzuri ila njia ambayo inatakiwa kutumika katika program yako ni kwa kutumia keyword inayoitwa with, unaanza na neno `with` kisha open() method na ndani unaweza 2 positional arguments na 1 keyword argument, kisha mwisho tunatumia neno as nje ya mabano na jin la object ambalo untaka kutumia kama open object inafrudisha.Mfano:

```py
with open("file.txt", 'w') as file_object:
    file_object.write("Hello, Python ni rahisi na nzuri")
    
file_object.close()

print(file_object.closed) # True
```

- kuna baadhi ya methods ambazo tunaweza kutumia katika Python ili handle errors mabzop zinatokea wakati wa kufunga na kufungua file.mfano ni `.closed` inarudisha kweli True kama file lako limekuwa closed kwa kutumia `.close()` method bna kinyume chake pia kama litakuwa halijafunmgwa.

| Character | Meaning                                                         |
| --------- | --------------------------------------------------------------- |
| 'r'       | open for reading (default)                                      |
| 'w'       | open for writing, truncating the file first                     |
| 'x'       | create a new file and open it for writing                       |
| 'a'       | open for writing, appending to the end of the file if it exists |
| 'b'       | binary mode                                                     |
| 't'       | text mode (default)                                             |
| '+'       | open a disk file for updating (reading and writing)             |


## Zingatia

- Hakikisha mode ya file lako iwe inaendana na kitu amabcho unataka kufanya katika program yako, kama unataka kusoma file mode yake itakuwa read `r` basi iwe inaendana na methods za file object yako ambayo unataka kufanya kwenye program yako.