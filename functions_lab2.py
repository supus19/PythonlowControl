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