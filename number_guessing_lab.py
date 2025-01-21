# this is my number guessing program
print('This is a Guessing Game')
print("Ready to play?")

number_2_guess = 7
print(number_2_guess)
user_guess= 5
user2_guess = 7
print(type(user_guess))
print(user_guess)
if number_2_guess == user_guess:
    print("Good guess guest1, you are a winner")
elif number_2_guess == user2_guess:
    print("Good guess guest2, you are a winner!")
else:
    print(str(user_guess) + " is not equal to " + str(number_2_guess))
