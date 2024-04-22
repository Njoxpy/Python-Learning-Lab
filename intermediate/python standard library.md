# Python Standard Library

- [Introduction](#introduction)
- [Working With Path](#working-with-path)
- [Working With Directories](#working-with-directories)
- [Working With Files](#working-with-files)
- [Workig With JSON Files](#workig-with-json-files)
- [Working With Database](#working-with-database)

## Introduction

- Python inakuja na baadhi ya libarray ambazo zipo kwenye program yako ambazo zinakuwezesha kuweza kufanya mambao fulani katika kuandika project katika program.Python inalist ya baadhi ya library ambazo ndio zinakuja na standard libraray ambazo zinkuwezesha kwa ajili ya shughuli mbalimbali katika program yako.

- Kuna libraray ambazo zinakuwezesha kwa ajili ya kufanya kazi na files, SQlITE, Date/Time, Random values, Emails.

## Working With Path

- Katika Python ili kuweza kutumia libraray kwa ajili ya kufannya kazi na Path inabidi iwe imported kwanza katika program yako.

```py
# import pathlib library
from pathlib import Path
```

- Kutoka kwenye mfano hapo juu tumechukua Parth object kutoka katika pathlib library.Kuna vit mbalimbali ambavyo unaweza kufanya na hio object kwenye program yako.

- `path.home`: Inarudisha home directory ya current user katika program yako.Inategemea na jina la home directory yako katika pc yako.

```py
from pathlib import Path
print(Path.home())
# Output: C:\Users\Mdudu
```

- `path.exists()`: Inatumika kuangalia kama njia(path) ipo au haipo kwenye program yako.

```py

```

- `path.is_file()`: Inatumika kuangalia path kama ni file au sio file inarudisha kweli kama ipo na kinyume cha haipo.

```py
```

- `pathis_dir()`: Inarudisha jibu kweli au sio kweli kama ni folder au sio katika mfuatano.

```py
```

- `path.suffix()`: Inarudisha list ya file extension katika hiyo path file,Kwa mfano tuna folder linaitwa `Django` na lina file zifuatazo, `file.txt`, `admin.py`, ukitumia .suffix itarudisha list ya extension ambazo zipo kwenye program yako ambazo ni `.txt` na `.py`.

```py

```

- `path.parent`: Inarudisha parent directory ya path ya hiyo file.

```py
```

- `path.absolute()`: Inarudisha absolute path ya hiyo file kwenye program yako

```py
```

## Working With Directories

- Directory ni sawa na folder, hivyo katika section hii nitaangazia je ni kwa namna gani tunaweza kufanya kazi na directories kwa kutumia Python.

- `Path.exists()`:Inatumika kuangalia kama path hiyo ya folder ipo kwenye program yako au haipo.

- `Path.mkdir()`:Inatumika kutengeneza folder, nisawa na kutumia

```sh
# in terminal
mkdir folderName

# using Python into IDE
Path.mkdir("FolderName")
```

- `Path.rmdir()`: Inatumika kwa ajili ya kufuta folder, ni sawa na kutumia rmdir kwenye terminal.

```sh
# using terminal
rmdir foldeName

# using Python
Path.rmdir()
```

- `Path.rename()`: Inatumika kwa ajili ya kubadili jina la directory.

- `Path.iterdir()`:Inatumika kwa ajili ya kupata list ya files na directory ambazo zipo kwenye hiyo njia(path).Kwa sababu iterdir inafanya iteration hivyo inatumika kwa ajili ya kupata idadi(list) ya files pamoja na folders ambazo zipo kwenye hiyo path.

```py
from pathlib import Path
currentPath = Path(r"C:\Users\Mdudu")
for p in currentPath.iterdir():
    print(p)
```

`iterdir()`, ni muhimu sana ila ina limitations, kama unahitaji kupata files ambazo zina extension ya `.py` haiwezekani ila kuna `Path.glob()` inakuwezesha kutafuta files na folders ambazo zina pattern fulani katika program yako mfano kama tunahitaji kupata list ya files zote zenye extension ya `.py` inabidi iwe hivi.

```py

```

## Working With Files

- `path.exists()`: Inarudisha true kama file lipo na kinume kama halipo, ndani yake inapita path ya hilo file'

```py
from pathlib import Path

if Path(r"C:\Users\Mdudu\Desktop\me.sh"):
    print("exists") # Output:exists
```

- `path.rename()`: Inachukua parameter moja ambayo ndio jina la file katika,ndani ya manbano ambayo yatakuwa ndani ya file utaweka jina la file ambalo ni jina baada ya kuwa renamed.

```py
from pathlib import Path

path = Path(r"C:\Users\Mdudu\Desktop\me.sh")
path.rename("redux.sh")
```

- `path.unlink()`:Kama unataka kufuta file utatumia unkink keyword.

```py

```

- `path.stat()`:Inarudisha takwimu kuhusu file kama size yake katika bytes, location, siku ambayo file lako limetengenezwa.

```py
from pathlib import Path

path = Path(r"C:\Users\Mdudu\Desktop\30 days of python\day 13\path.py")
print(path.stat())

# Output: os.stat_result(st_mode=33206, st_ino=9007199254818323, st_dev=2728893878, st_nlink=1, st_uid=0, st_gid=0, st_size=118, st_atime=1713797285, st_mtime=1713797282, st_ctime=1713796378)
```

- `path.read_bytes()`:Inarudisha content ambazo zipo kwenye hiyo path ambapo content hizo zinakuwa katika bytes.

```py
from pathlib import Path

path = Path(r"C:\Users\Mdudu\Desktop\30 days of python\day 13\path.py")

print(path.read_bytes())
```

- `path.read_text()`: Inarudisha content ambazo zipo kwenye hiyo path ambapo content hizo zinakuwa katika maneno (string format).

```py
from pathlib import Path

path = Path(r"C:\Users\Mdudu\Desktop\30 days of python\day 13\path.py")

print(path.read_text())
```

## Workig With JSON Files

- JSON Inasimama badala ya JavaScript object notation ni namna ya kutuma data kama human readable format.Katika Python unauwezo wa kufanya kazi na json files kwa kutumia json module.

```py
import json
# import json module

# create movie dictionary for json data
article = [
    {
    "id":1,
    "Title": "Python Standard Library Essentials",
    "Author": "Mdudu",
    "Category": "Python"
    }
]

# using json modules to dump movie object
data = json.dumps(article)
print(data)
```

## Working With Database

## Articles

- [Python PathLib.](https://docs.python.org/3/library/pathlib.html)
- [Python Standard Library]()
