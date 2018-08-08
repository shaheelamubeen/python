
######TUPLE
phones=("iphone", "oppo", "jio")
>>> phones
('iphone', 'oppo', 'jio')
>>> phone[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'phone' is not defined
>>> phones[1]
'oppo'
>>> phones[1]='lio'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> phones=("iphone", "oppo", "jio", "blackberry"))
  File "<stdin>", line 1
    phones=("iphone", "oppo", "jio", "blackberry"))
                                                  ^
SyntaxError: invalid syntax
>>> phones=("iphone", "oppo", "jio", "iphone")
>>> phones
('iphone', 'oppo', 'jio', 'iphone')
>>> languages=tuple(("marathi", "hindi", "english"))
>>> languages
('marathi', 'hindi', 'english')
>>> len(phones)
4

