#!/usr/bin/env python
# coding: utf-8
Number 1 -

Question -
Create an assert statement that throws an AssertionError if the variable spam is a negative integer.

Answer -
spam = -55
assert spam > 0, 'The spam variable is is a negative integer.'
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-7-d8f84495732b> in <module>
      1 spam = -55
----> 2 assert spam > 0, 'The spam variable is is a negative integer.'

AssertionError: The spam variable is is a negative integer.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

Answer -
eggs = 'hello'
bacon = 'Hello'

assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!' 
assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-13-53586d290ac7> in <module>
      2 bacon = 'Hello'
      3 
----> 4 assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!'
      5 assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'

AssertionError: The eggs and bacon variables are the same!
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
Create an assert statement that throws an AssertionError every time.

Answer -
assert False, 'This assertion always triggers.'

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
What are the two lines that must be present in your software in order to call logging.debug()?

Answer -
To be able to call logging.debug(), you must have these two lines at the start of your program:

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

Answer -
To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:

import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
What are the five levels of logging?

Answer -
DEBUG, INFO, WARNING, ERROR, and CRITICAL

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
What line of code would you add to your software to disable all logging messages?

Answer -
logging.disable(logging.CRITICAL)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
Why is using logging messages better than using print() to display the same message?

Answer -
You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

Answer -
The Step button will move the debugger into a function call. The Over button will quickly execute the function call without stepping into it. The Out button will quickly execute the rest of the code until it steps out of the function it currently is in.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 10 -

Question -
After you click Continue, when will the debugger stop ?

Answer -
After you click Continue, the debugger will stop when it has reached the end of the program or a line with a breakpoint.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 11-

Question -
What is the concept of a breakpoint?

Answer -
Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line