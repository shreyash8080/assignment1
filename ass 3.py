#!/usr/bin/env python
# coding: utf-8
Number 1 -

Question -
Why are functions advantageous to have in your programs?

Answer -
Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
When does the code in a function run: when it's specified or when it's called?

Answer -
The code in a function executes when the function is called, not when the function is defined.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
What statement creates a function?

Answer -
The def statement defines, i.e. creates a function.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
What is the difference between a function and a function call?

Answer -
A function consists of the def statement and the code in its def clause. A function call is what moves the program execution into the function, and the function call evaluates to the function's return value.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
How many global scopes are there in a Python program? How many local scopes?

Answer -
There is one global scope, and a local scope is created whenever a function is called.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
What happens to variables in a local scope when the function call returns?

Answer -
When a function returns, the local scope is destroyed, and all the variables in it are forgotten.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
What is the concept of a return value? Is it possible to have a return value in an expression?

Answer -
A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
If a function does not have a return statement, what is the return value of a call to that function?

Answer -
If there is no return statement for a function, its return value is None.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
How do you make a function variable refer to the global variable?

Answer -
A global statement will force a variable in a function to refer to the global variable.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 10 -

Question -
What is the data type of None?

Answer -
The data type of None is NoneType.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 11-

Question -
What does the sentence import areallyourpetsnamederic do?

Answer -
That import statement imports a module named areallyourpetsnamederic.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 12 -

Question -
If you had a bacon() feature in a spam module, what would you call it after importing spam?

Answer -
This function can be called with spam.bacon().

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 13 -

Question -
What can you do to save a programme from crashing if it encounters an error?

Answer -
Place the line of code that might cause an error in a try clause.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 14 -

Question -
What is the purpose of the try clause? What is the purpose of the except clause?

Answer -
The code that could potentially cause an error goes in the try clause.
-The code that executes if an error happens goes in the except clause