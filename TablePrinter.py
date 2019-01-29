Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> spam = "That is Alice's cat"
>>> spam = 'That is Alice\'s cat'
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/catnapping.py 
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/catnapping.py 
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> 'Hello' in 'Hello World!'
True
>>> spam
'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/validateInput.py 
Enter your age:
l
Please enter a number for your age.
Enter your age:
16
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/picnicTable.py 
---PICNIC ITEMS--
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/picnicTable.py", line 7, in <module>
    printPicnic(picnicItems, 12, 5)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/picnicTable.py", line 4, in printPicnic
    print(k.ljust(leftWidth,'.') + str(v).rjust(rightwidth))
NameError: name 'rightwidth' is not defined
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/picnicTable.py 
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/picnicTable.py 
--PICNIC ITEMS-
sandwiches..  4
apples...... 12
cups........  4
cookies.....8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/picnicTable.py 
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
>>> import pyperclip
>>> pyperclip.copy('Hello World!')
>>> pyperclip.paste()
'Hello World!'
>>> pyperclip.paste()
'For example, if I copied this sentence to the clipboard and then called paste(), it would look like this:'
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/pw.py 
Usage: python pw.py [account] - copy acount password
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/pw.py 
Usage: python pw.py [account] - copy acount password
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/pw.py 
Press enter to quit
Usage: python pw.py [account] - copy acount password
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/bulletPointAdder.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/bulletPointAdder.py", line 9, in <module>
    lines = text.plit('\n')
AttributeError: 'str' object has no attribute 'plit'
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/bulletPointAdder.py 
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 8, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 6, in printTable
    colWidths = [0] * len(TableData)
NameError: name 'TableData' is not defined
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
[0, 0, 0]
>>> len('apples')
6
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 11, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 7, in printTable
    big = max(len(TableData[0]))
TypeError: 'int' object is not iterable
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
4
[0, 0, 0]
>>> tabeleData[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tabeleData[0]
NameError: name 'tabeleData' is not defined
>>> tableData[0]
['apples', 'oranges', 'cherries', 'banana']
>>> tableData[0][0]
'apples'
>>> len(tableData[0][0])
6
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
5
[0, 0, 0]
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
5
[8, 5, 5]
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 15, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 13, in printTable
    print(TableData.rjust(colWidths, ''))
AttributeError: 'list' object has no attribute 'rjust'
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 15, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 13, in printTable
    print(TableData[1].rjust(colWidths[1], ''))
AttributeError: 'list' object has no attribute 'rjust'
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 15, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 13, in printTable
    print(TableData[1].rjust(colWidths[1],' '))
AttributeError: 'list' object has no attribute 'rjust'
>>> print(tableData)
[['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'goose']]
>>> print(tableData[0])
['apples', 'oranges', 'cherries', 'banana']
>>> print(tableData[0][0].rjust(20, '*'))
**************apples
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 16, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 14, in printTable
    print(TableData[i][k].rjust(colWidths[i], ''))
TypeError: The fill character must be exactly one character long
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
 oranges
cherries
  banana
Alice
  Bob
Carol
David
 dogs
 cats
moose
goose
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
 oranges
cherries
  banana
Alice
  Bob
Carol
David
 dogs
 cats
moose
goose
>>> range(3)
range(0, 3)
>>> tableData[range(2)][0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tableData[range(2)][0]
TypeError: list indices must be integers or slices, not range
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
 oranges
cherries
  banana
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 18, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 14, in printTable
    for k,v in range(len(TableData[0])):
TypeError: cannot unpack non-iterable int object
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
Traceback (most recent call last):
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 18, in <module>
    printTable(tableData)
  File "C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py", line 14, in printTable
    for k,v in range(len(TableData[0])):
TypeError: cannot unpack non-iterable int object
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
 oranges
cherries
  banana
>>> k in tableData
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    k in tableData
NameError: name 'k' is not defined
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
3
 oranges
3
cherries
3
  banana
3
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
range(0, 3)
 oranges
range(0, 3)
cherries
range(0, 3)
  banana
range(0, 3)
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples
 oranges
cherries
  banana
  apples
 oranges
cherries
  banana
  apples
 oranges
cherries
  banana
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  applesAlice
 oranges  Bob
cherriesCarol
  bananaDavid
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples Alice
 oranges   Bob
cherries Carol
  banana David
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples Alice dogs
 oranges   Bob cats
cherries Carolmoose
  banana Davidgoose
>>> 
 RESTART: C:/Users/Roy/AppData/Local/Programs/Python/Python37/AutomateTheBoringStuff/AutomateTheBoringStuff/printTable.py 
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
>>> 
