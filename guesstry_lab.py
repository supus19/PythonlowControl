#this is my number guessing game
print('This is a number Guessing Game')
print("Ready to play")

guess_number = 6
user_input = input("Guess a number from 0 to 10: ")
try:
    user_input = int(user_input)
except:
    print(user_input, 'is not a number')
else:
    if guess_number == int(user_input):
        print("Good guess, you are a winner")
    elif guess_number+1 == int(user_input) or guess_number-1 == int(user_input):
        print("Close but no cigar. You are 1 away from the guess: 6")
    else:
        print(str(user_input) +  " is not equal to " + str(guess_number) + ". Better luck next time!")