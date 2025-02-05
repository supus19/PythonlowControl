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

print("Lab 5")

# Using the ord() function to find the hex value of the 'Ω' symbol
ohm_symbol = 'Ω'
hex_value = hex(ord(ohm_symbol))  # Convert to hexadecimal

print(f"The hex value of 'Ω' is: {hex_value}")  # Output: 0x3a9

# Ohm's Law: R = V / I
# Given: Voltage (V) = 5V, Current (I) = 20mA (0.020A)

volts = 5
current = 0.020  # 20mA converted to Amperes
resistance = volts / current  # R = V / I

# Using chr() to print the Ω symbol
print(f"A circuit with a voltage of {volts}V and a current of {current * 1000}mA will require a resistor of {resistance}{chr(937)}")

# Asking the user for voltage and current to dynamically calculate resistance
volts = float(input("Enter voltage (V): "))
current = float(input("Enter current (mA): ")) / 1000  # Convert mA to A
resistance = volts / current

# Displaying the result with the Ω symbol
print(f"A circuit with a voltage of {volts}V and a current of {current * 1000}mA will require a resistor of {resistance}{chr(937)}")

print("lab 6")

def multiply(x, y):
    return x*y

def sum(x, y):
     add = x+y
     if (add//2 != 0):
      add+=1
      return add
     

print("lab 7")

# Function to perform mathematical operations
def my_math(x, y, operation="Addition"):
    if operation == "Addition":
        result = x + y
        symbol = "+"
    elif operation == "Subtraction":
        result = x - y
        symbol = "-"
    elif operation == "Multiplication":
        result = x * y
        symbol = "*"
    elif operation == "Division":
        if y == 0:  # Handling division by zero
            return "Error: Division by zero is not allowed."
        result = x / y
        symbol = "/"
    else:
        return "Error: Invalid operation."

    return f"The result of {x} {symbol} {y} = {result}"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter valid number")

print("Lab 8")

# Function to return greetings in different languages
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'sw':
        return 'Habari'  # Swahili
    elif lang == 'uk':
        return 'Привіт'  # Ukrainian (Pryvit)
    elif lang == 'elv':
        return 'Mae govannen'  # Middle Earth Elven (Sindarin)
    elif lang == 'tlh':
        return 'nuqneH'  # Klingon (means "What do you want?")
    else:
        return 'Hello'



def main():
      num1 = 5
      num2 = 10
      multiplication = multiply(num1, num2)
      print(multiplication)
      summation = sum(num1, num2)
      print(summation)

      mynum1 = get_number("Enter the first number: ")
      mynum2 = get_number("Enter the second number: ")

      operations = ["Addition", "Subtraction","Multiplication", "Division"]
      print("Choose an operations: ", ", ".join(operations))
      while True:
          operation = input("Enter the operation: ").strip().capitalize()
          if operation in operations:
              break
          print("Invalid Operation. Try again")

      result = my_math(mynum1, mynum2, operation)
      print(result)

      print(greet('en'), 'Glenn')
      print(greet('fr'), 'Sabine')
      print(greet('es'), 'Carlos')
      print(greet('sw'), 'Amina')
      print(greet('uk'), 'Andriy')
      print(greet('elv'), 'Legolas')
      print(greet('tlh'), 'Worf')

      name = input("\nWhat is your name? ")
    
      print("\nAvailable languages: English (en), Spanish (es), French (fr), Swahili (sw), Ukrainian (uk), Elven (elv), Klingon (tlh)")
      language = input("Choose your language code: ").strip().lower()

      print(f"{greet(language)}, {name}!")


main()