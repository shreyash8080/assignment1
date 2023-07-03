#!/usr/bin/env python
# coding: utf-8
Number 1 -

Question -
Is the Python Standard Library included with PyInputPlus?

Answer -
PyInputPlus is a Python module used for taking inputs with additional validation features. PyInputPlus will keep asking the user for text until they enter valid input.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
Why is PyInputPlus commonly imported with import pyinputplus as pypi?

Answer -
The 'as pypi' code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus function.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
How do you distinguish between inputInt() and inputFloat()?

Answer -
"inputInt()" : Accepts an integer value. This also takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’ for bounds. Returns an int. "inputFloat()" : Accepts a floating-point numeric value. Also takes additional ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’ parameters. Returns a float.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

Answer -
# In[5]:


pip install pyinputplus


# In[6]:


import pyinputplus as pypi
  
# integer input with
# specific bounds
inp = pypi.inputInt(prompt = "Enter an Integer... ",min = 0, max = 99 )
  
print(inp)

Number 5 -

Question -
What is transferred to the keyword arguments allowRegexes and blockRegexes?

Answer -
The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
If a blank input is entered three times, what does inputStr(limit=3) do?

Answer -
It will raise RetryLimitException.
# In[7]:


np = pypi.inputStr(limit=3)

Number 7 -

Question -
If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

Answer -
The function returns the default value instead of raising an exception.
# In[8]:


inp = pypi.inputStr(limit=3, default='hello')


# In[9]:


inp


# In[ ]:




