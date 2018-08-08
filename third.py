###set
subjects={"biology", "zoology", "botony"}
>>> subjects
{'zoology', 'botony', 'biology'}
>>> subjects.add("chemistry")
>>> subjects
{'zoology', 'botony', 'chemistry', 'biology'}
>>> subjects.add("biology")
>>> subjects
{'zoology', 'botony', 'chemistry', 'biology'}
>>> subjects=("biology", "zoology", "botony")




###dictionary
computer={
...     "type":"pc",
...     "color":"black",
...     "used":"home"
... }
>>> computer
{'used': 'home', 'color': 'black', 'type': 'pc'}
>>> compoter['used']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'compoter' is not defined
>>> compoter['type']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'compoter' is not defined
>>> computer['type']
'pc'
>>> computer[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> 
