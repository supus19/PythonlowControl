print('Using the function int() & type() & id()')
user_input = input('enter a number > ')
print(user_input)
print(type(user_input))
print('the id() of user_input as a str', id( user_input))
print(ord(user_input))
user_input = int(user_input)
print(type(user_input))
print('the id() of user_input as a int', id( user_input))

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

