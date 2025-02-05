print('Playing with Builtin Python Functions')
student_name = "Saaketh Shanbhogue"
program_creation_date = "02/05/2025"
print(student_name)
print(program_creation_date)

print('''This Lab is about using Python Builtin Functions. Try and show code using the following functions, then pick 4 more to try. ...
- print()
- input('enter something here: ')
- int()
- type()
- abs()
- len()

My code follows:''')

print('Using the function int() & type() & id()')
user_input = input('enter a number > ')
print(user_input)
print(type(user_input))
print('the id() of user_input as a str', id( user_input))
print(ord(user_input))
user_input = int(user_input)
print(type(user_input))
print('the id() of user_input as a int', id( user_input))
print(len(student_name))

def print_lyrics():
  print("Tonight you're falling in love")
  print("Let me go now")
  print("This feeling's tearing me up")
  print("Here we go now")
  print("Come on,")

def print_chorus():
  print("Shake, shake")
  print("Shake, shake, shake it")

def greet(lang):
    if lang == 'es':
        return'Hola'
    elif lang == 'fr':
        return'Bonjour'
    else:
        return'Hello'

def main() :  
    print('Part of Shake it by Metro Station')
    print_lyrics()
    print_chorus()
    print_chorus()
    print_chorus()
    print_chorus()
    print_chorus()

    print(greet('en'),'Glenn')
    print(greet('fr'),'Sabine')
    print(greet('es'),'Carlos')
  
main()



