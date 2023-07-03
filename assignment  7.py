#!/usr/bin/env python
# coding: utf-8
Number 1 -

Question -
What is the name of the feature responsible for generating Regex objects?

Answer -
The name of the feature responsible for generating Regex objects is re.compile() function which returns Regex objects.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
Why do raw strings often appear in Regex objects?

Answer -
Raw strings are used so that backslashes do not have to be escaped.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
What is the return value of the search() method?

Answer -
the return value of the search() method is that it returns Match objects.The search() function searches the string for a match, and returns a Match object if there is a match.
# In[1]:


import re

data = "This is iNeuron Full Stack Data Science Class"
x = re.search("i", data)

print("The first i character is located in position:", x.start()) 
type(x)

Number 4 -

Question -
From a Match item, how do you get the actual strings that match the pattern?

Answer -
The group() method returns strings of the matched text.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?

Answer -
Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?

Answer -
Periods and parentheses can be escaped with a backslash: \

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?

Answer -
If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
In standard expressions, what does the | character mean?

Answer -
The | character signifies matching "either, or" between two groups.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
What two things does the ? character signify in regular expressions?

Answer -
The ? character can either mean "match zero or one of the preceding group" or be used to signify nongreedy matching.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 10 -

Question -
In regular expressions, what is the difference between the + and * characters?

Answer -
The + matches one or more. The * matches zero or more.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 11-

Question -
What is the difference between {4} and {4,5} in regular expression?

Answer -
The {4} matches exactly three instances of the preceding group. The {4,5} matches between four and five instances.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 12 -

Question -
What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?

Answer -
The \d, \w, and \s shorthand character classes match a single digit, word, or space character, respectively.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 13 -

Question -
What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

Answer -
The \D, \W, and \S shorthand character classes match a single character that is not a digit, word, or space character, respectively.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 14 -

Question -
What is the difference between .* and .*??

Answer -
The .* performs a greedy match, and the .*? performs a nongreedy match.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 15 -

Question -
What is the syntax for matching both numbers and lowercase letters with a character class?

Answer -
Either [0-9a-z] or [a-z0-9]

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 16 -

Question -
What is the procedure for making a normal expression in regex case insensitive?

Answer -
Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 17 -

Question -
What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?

Answer -
The . character normally matches any character except the newline character. If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 18 -

Question -
If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?


# In[3]:


import re
numRegex = re.compile(r'\d+')                  
numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')

Number 19 -

Question -
What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

Answer -
The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 20 -

Question -
How would you write a regex that match a number with comma for every three digits? It must match the given following:

'42'
'1,234'
'6,368,745'
but not the following:
'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
Answer -
re.compile(r'^\d{1,3}(,\d{3})*$') will create this regex, but other regex strings can produce a similar regular expression.