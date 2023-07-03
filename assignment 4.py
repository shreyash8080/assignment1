#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Number 1 -

Question -
What exactly is []?

Answer -
The empty list value, which is a list value that contains no items.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

Answer -
spam[2] = 'hello'

spam = [2, 4, 6, 8, 10]
spam[2] = 'hello' 
spam
[2, 4, 'hello', 8, 10]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

Number 3 -

Question -
What is the value of spam[int(int('3' * 2) / 11)]?

Answer -
spam = ['a', 'b', 'c', 'd']
spam[int(int('3' * 2) / 11)]
'd'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
What is the value of spam[-1]?

Answer -
spam[-1]
'd'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
What is the value of spam[:2]?

Answer -
spam[:2]
['a', 'b']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.

bacon = [3.14, 'cat', 11, 'cat', True]
Number 6 -

Question -
What is the value of bacon.index('cat')?

Answer -
bacon.index('cat')
1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
What does bacon.append(99) change the look of the list value in bacon?

Answer -
bacon.append(99)
bacon
[3.14, 'cat', 11, 'cat', True, 99]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
How does bacon.remove('cat') change the look of the list meaning in bacon?

Answer -
bacon.remove('cat') 
bacon
[3.14, 11, 'cat', True, 99]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
What are the list concatenation and list replication operators?

Answer -
The operator for list concatenation is +, while the operator for replication is *.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 10 -

Question -
What is difference between the list methods append() and insert()?

Answer -
While append() will add values only to the end of a list, insert() can add them anywhere in the list.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 11-

Question -
What are the two methods for removing items from a list?

Answer -
The del statement and the remove() list method are two ways to remove values from a list.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 12 -

Question -
Describe how list values and string values are identical.

Answer -
Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 13 -

Question -
What's the difference between tuples and lists?

Answer -
Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 14 -

Question -
How do you type a tuple value that only contains the integer 42?

Answer -
(42)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 15 -

Question -
How do you get a list value's tuple form? How do you get a tuple value's list form?

Answer -
The tuple() and list() functions, respectively

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 16 -

Question -
Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

Answer -
They contain references to list values.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 17 -

Question -
How do you distinguish between copy.copy() and copy.deepcopy()?

Answer -
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

