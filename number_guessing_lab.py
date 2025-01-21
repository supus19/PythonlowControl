
#this is my number guessing program

print("This is a Guessing Game")
print("Ready to play?")


#if the user guess is equal to the number, the user is a winner
#there are two users who are competing
number_2_guess = 7
print(number_2_guess)
user_guess= input("User #1 guess: ")
user2_guess = input("User #2 guess: ")

 
if number_2_guess == int(user_guess):
    print("Good guess guest1, you are a winner")
elif number_2_guess == int(user2_guess):
    print("Good guess guest2, you are a winner!")
else:
    print(str(user_guess) + " or " + str(user2_guess) + " are not equal to " + str(number_2_guess) + ". Better luck next time!")