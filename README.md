#Auto Select Course System For TTU
This is a convenient system for TTU student to select their course in easy, fast, convenient way.

##What You Need:

Python3.5.1 & requests

[Download Python3.5.1](https://www.python.org/downloads/release/python-351/)

[Install requests](http://docs.python-requests.org/en/latest/)

##HOW TO USE:

1.請先將你想選取的課程代碼，利用notepad建立成寫入config.conf檔，並將之至於Autoselect.py同目錄

EX:
```
CourseList = ["G1410A","G1410B","G1430G","G1612O"]
...
```
2.執行，在命令提示字元或終端機下輸入:

MAC \ Linux:
```
python3 Autoselect.py
```
Windows:
```
python Autoselect.py
```
3.按照指示進行

##免責聲明:

此工具目前屬於開發階段，部分功能正常，使用者須承擔一切風險(我不保證能選上你所想要的課，中間有太多因素...)

##Changelog:
####2014/3/21 ASCS 0.1 Nightly Build:

1. Under command/Terminal.
2. Can login ttu student information system successfully.

####2014/3/22 ASCS 0.2 Nightly Build:

1. Login Function Created.
2. big5 decode.
3. utf-8 decode.
4. Can read selected list.

####2014/5/2  ASCS 1.0ver:

1. Select Course Function finish.
2. CountDown Function finish.
3. read selected list(beta).

####2015/1/18 ASCS by requests 1.0 ver.

1. Change urllib to requests
2. CountDown function is unavailable now(it will be fixed)

####2016/1/21 ASCS by requests 2.0 ver.
1. Add read configuer file.
2. Fix countdown function.
3. Multithreading programing

######by JasonPan

