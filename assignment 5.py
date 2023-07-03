#!/usr/bin/env python
# coding: utf-8
# Number 1 -

Question -
What does an empty dictionary's code look like?

Answer -
An empty dictionary's code look like two curly brackets: {}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
What is the value of a dictionary value with the key 'foo' and the value 42?

Answer -
The value of a dictionary value with the key 'foo' and the value 42 is {'foo': 42}

dic = {'foo' : 42}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
What is the most significant distinction between a dictionary and a list?

Answer -
The items in a list are ordered items, while the items stored in a dictionary are unordered

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
What happens if you try to access spam['foo'] if spam is {'bar': 100}?

spam = {'bar': 100}
spam['foo']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-56a8e50c7ff8> in <module>
      1 spam = {'bar': 100}
----> 2 spam['foo']

KeyError: 'foo'
- Answer -

We will get a KeyError error.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

Answer -
There is no difference. The in operator checks whether a value exists as a key in the dictionary.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

Answer -
'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
What is a shortcut for the following code?

if 'color' not in spam:
spam['color'] = 'black'
Answer -
spam.setdefault('color', 'black')

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
How do you "pretty print" dictionary values using which module and function?

Answer -
pprint.pprint()