age=4
if age==3:
    print("you can get admission in school")
elif age==4:
    print("you have entered school last year")
    else:
    print("youcannot get admission)
    age=4
if age==3:
    print("you can get admission in school")
elif age==4:
     print("you have entered school last year")
else:
     print("youcannot get admission") 
     age=4
>>> if age==3:
...     print("you can get admission in school")
... elif age==4:
...     print("you have entered school last year")
... else:
...     print("youcannot get admission)
  File "<stdin>", line 6
    print("youcannot get admission)
                                  ^
SyntaxError: EOL while scanning string literal
>>> age=4
>>> if age==3:
...     print("you can get admission in school")
... elif age==4:
...      print("you have entered school last year")
... else:
...      print("youcannot get admission") 
... 
you have entered school last year
>>> pens=["flair", "renolds", "technotip", "pinpoint"]
>>> pens
['flair', 'renolds', 'technotip', 'pinpoint']
>>> pens[2]
'technotip'
>>> pens[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> pens[3]
'pinpoint'
>>> pens=list(("flair", "renolds", "technotip", "pinpoint"))
>>> pens
['flair', 'renolds', 'technotip', 'pinpoint']
>>> pens.remove("technotip")
>>> pens
['flair', 'renolds', 'pinpoint']
>>> pens.("technotip")
  File "<stdin>", line 1
    pens.("technotip")
         ^
SyntaxError: invalid syntax
>>> pens.("finegrip")
  File "<stdin>", line 1
    pens.("finegrip")
         ^
SyntaxError: invalid syntax
>>> pens.append("finegrip")
>>> pens
['flair', 'renolds', 'pinpoint', 'finegrip']
>>> len(pens)
4
>>> pens.sort
<built-in method sort of list object at 0x1021d7208>
>>> pens.sort()
>>> pens
['finegrip', 'flair', 'pinpoint', 'renolds']
>>> pens.reverse()
>>> pens
['renolds', 'pinpoint', 'flair', 'finegrip']
>>> pens.pop(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> pens.pop(3)
'finegrip'
>>> pens.pop(1)
'pinpoint'
>>> pens
['renolds', 'flair']
>>> pens.index("flair)
  File "<stdin>", line 1
    pens.index("flair)
                     ^
SyntaxError: EOL while scanning string literal
>>> pens.index("flair")
1
>>> pens.insert(1,"pinpoint")
>>> pens
['renolds', 'pinpoint', 'flair']
>>> pens
['renolds', 'pinpoint', 'flair']
>>> pens.clear()
>>> pens
[]
>>> 
