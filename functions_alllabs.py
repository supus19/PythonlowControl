# Functions Introduction
# Python Lab - Functions - min() max()
print('Playing with Builtin Python Functions')
print('min() max()')
student_name = "Saaketh Shanbhogue"
program_creation_date = "02/05/2025"
print(student_name)
print(program_creation_date)
print('''Functions Introduction
There is a big list of built-in functions here:
https://www.w3schools.com/python/python_ref_functions.asp
''') 
print('''This Lab is about using Python Builtin Functions min() and max().
Try and show code using the following functions:
- max()
- min()

My code follows:''')

my_string = input("Enter a long string: ")
print('The variable "my_string" = ',my_string)
biggest = max(my_string)
print('The biggest character in the \nstring "STEAM Is Cool" is',biggest)
smallest = min(my_string)
print('The smallest character in the \nstring "STEAM Is Cool" is',smallest)


print('''Functions ord() chr()
There is a big list of built-in functions here:
https://www.w3schools.com/python/python_ref_functions.asp
''')      
print('''
Challenge #1
      
Hola, Mi nombre es Iñigo Montoya
Tú mataste a mi padre. Prepárate a morir
      
Note the special charaters in the spanish text
      
Using the Extended ASCII table
link --> https://www.ascii-code.com/
and the built-in Functions
- ord()    - convert a number or character to it's unicode value
- chr()    - convert a unicode value to it printable character

Using the chr() function, complete the sentence with the correct 
accented characters in the 2nd line in the example above.  
      ''')
print('''
Enter Your Code Here:
----------------------------------------------------
''')
print('Hola, Mi nombre es I' + str(chr(0xf1)) + 'igo Montoya')
print('Tu mataste a mi padre. Preparate a morir')


print('''Functions ord() chr()
There is a big list of built-in functions here:
https://www.w3schools.com/python/python_ref_functions.asp
''')      
print('''
Challenge #1
      
Hola, Mi nombre es Iñigo Montoya
Tú mataste a mi padre. Prepárate a morir
      
Note the special characters in the Spanish text
      
Using the Extended ASCII table
link --> https://www.ascii-code.com/
and the built-in Functions
- ord()    - convert a number or character to its Unicode value
- chr()    - convert a Unicode value to its printable character

Using the chr() function, complete the sentence with the correct 
accented characters in the 2nd line in the example above.  
''')
print('''
Enter Your Code Here:
----------------------------------------------------
''')

print('Hola, Mi nombre es I' + chr(241) + 'igo Montoya')  # ñ -> chr(241)
print('T' + chr(250) + ' mataste a mi padre. Prep' + chr(225) + 'rate a morir') 

print('''Functions Introduction
There is a big list of built-in functions here:
https://www.w3schools.com/python/python_ref_functions.asp
''')      

print('''
Challenge #1
Write some code that uses the following built-in functions.
Run, then edit the code in the template example:
      
Using some built-in Functions:
- abs()    - try some equation like x=(4+5)*-7
- bin()    - change a decimal number to its binary
- ord()    - convert a number or character to its Unicode value
- chr()    - convert a Unicode value to its printable character
- round()  - Do some math, get a long floating point number and
             round it. Then round it to 2 significant digits
- Pick 3 more functions and try them...
- Still have time? Pick 3 more!      
''')

print('''
Be sure to document your code with comments.
Hint: Check out W3Schools Functions:
- https://www.w3schools.com/python/python_ref_functions.asp

Enter Your Code Here:
----------------------------------------------------
''')

# abs() - Get the absolute value of a number
x = (4 + 5) * -7
print("Absolute value of x:", abs(x))  # Output: 63

# bin() - Convert a decimal number to binary
decimal_number = 25
print("Binary representation of 25:", bin(decimal_number))  # Output: 0b11001

# ord() - Get the Unicode value of a character
char = 'A'
print("Unicode of 'A':", ord(char))  # Output: 65

# chr() - Convert a Unicode value to its character
unicode_value = 241
print("Character for Unicode 241:", chr(unicode_value))  # Output: ñ

# round() - Round a floating-point number
float_num = 12.3456789
print("Rounded number:", round(float_num))  # Output: 12
print("Rounded to 2 decimal places:", round(float_num, 2))  # Output: 12.35

# len() - Get the length of a string
text = "Python Programming"
print("Length of text:", len(text))  # Output: 18

# max() - Find the maximum value in a list
numbers = [3, 8, 1, 12, 5]
print("Maximum value in the list:", max(numbers))  # Output: 12

# min() - Find the minimum value in a list
print("Minimum value in the list:", min(numbers))  # Output: 1

# sum() - Get the sum of all elements in a list
print("Sum of all numbers:", sum(numbers))  # Output: 29

# pow() - Calculate power (base^exponent)
print("2 raised to the power of 3:", pow(2, 3))  # Output: 8

# type() - Get the data type of a variable
print("Data type of float_num:", type(float_num))  # Output: <class 'float'>

# str() - Convert a number to a string
number = 100
print("String representation of 100:", str(number))  # Output: '100'

# print('Done with Challenge 1')
