JavaScript - Warm up
This is the introduction to the basics of Javascript.
Background Context
JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

Scripting (same as we did with Python)
Web front-end
For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

RESOURCES

Writing JavaScript Code(https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
Variables(https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
Data Types(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
Operators(https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
Operator Precedence(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)
Controlling Program Flow(https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
Functions(https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
Objects and Arrays(https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
Intrinsic Objects(https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
Module patterns(https://darrenderidder.github.io/talks/ModulePatterns/#/)
var, let and const(https://www.youtube.com/watch?v=sjyJBL5fkp8&ab_channel=FunFunFunction)
JavaScript Tutorial(https://www.youtube.com/watch?v=vZBCTc9zHtI&ab_channel=LearnCode.academy)
Modern JS(https://github.com/mbeaudru/modern-js-cheatsheet)

General
Why JavaScript programming is amazing
How to run a JavaScript script
How to create variables and constants
What are differences between var, const and let
What are all the data types available in JavaScript
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use while and for loops
How to use break and continue statements
What is a function and how do you use functions
What does a function that does not use any return statement return
Scope of variables
What are the arithmetic operators and how to use them
How to manipulate dictionary
How to import a file

Task 0.
Write a script that prints “JavaScript is amazing”:

You must create a constant variable called myVar with the value “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var

Task 1. 
Write a script that prints 3 lines:

The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var

Task 2.
Write a script that prints a message depending of the number of arguments passed:

If no arguments are passed to the script, print “No argument”
If only one argument is passed to the script, print “Argument found”
Otherwise, print “Arguments found”
You must use console.log(...) to print all output
You are not allowed to use var
Reference: process.argv

Task 3.
Write a script that prints the first argument passed to it:

If no arguments are passed to the script, print “No argument”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use length

Task 4.
Write a script that prints two arguments passed to it, in the following format: “ is ”

You must use console.log(...) to print all output
You are not allowed to use var

Task 5.
Write a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use try/catch

Task 6.
Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop

The first line: “C is fun”
The second line: “Python is cool”
The third line: “JavaScript is amazing”
You must use console.log(...) to print all output
You are not allowed to use var
You are not allowed to use any if/else statement
You can use only one console.log
You must use a loop (while, for, etc.)

Task 7.
Write a script that prints x times “C is fun”

Where x is the first argument of the script
If the first argument can’t be converted to an integer, print “Missing number of occurrences”
You must use console.log(...) to print all output
You are not allowed to use var
You can use only two console.log
You must use a loop (while, for, etc.)

Task 8.
Write a script that prints a square

The first argument is the size of the square
If the first argument can’t be converted to an integer, print “Missing size”
You must use the character X to print the square
You must use console.log(...) to print all output
You are not allowed to use var
You must use a loop (while, for, etc.)

Task 9.
Write a script that prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
You must use console.log(...) to print all output
You are not allowed to use var

Task 10.
Write a script that computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
You must do it recursively
You must use a function
You must use console.log(...) to print all output
You are not allowed to use var

Task 11.
Write a script that searches the second biggest integer in the list of arguments.

You can assume all arguments can be converted to integer
If no argument passed, print 0
If the number of arguments is 1, print 0
You must use console.log(...) to print all output
You are not allowed to use var

Task 12. 
Update this script to replace the value 12 with 89:

You are not allowed to use var

Task 13. 
Write a function that returns the addition of 2 integers.

The function must be visible from outside
The name of the function must be add
You are not allowed to use var

Task 14. 
Write a file that modifies the value of myVar to 333

Task 15.
Write a function that executes x times a function.

The function must be visible from outside
Prototype: function (x, theFunction)
You are not allowed to use var

Task 16.
Write a function that increments and calls a function.

The function must be visible from outside
Prototype: function (number, theFunction)
You are not allowed to use var

Task 17.
Update this script by adding a new function incr that increments the integer value.

You are not allowed to use var
