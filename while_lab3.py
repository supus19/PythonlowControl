while True:
    try:
        x = int(input("Input a number greater than 20: "))
    except:
        print("Invalid input. Please enter a whole number")
    else:
        print(x)
        print("Your number ", x, " is a valid integer greater than 20. Thansk")
        break
count = 0
while x > 1:
    x=x/2
    print("Current value of user input is ",x )
    count+=1
print("While loop looped ", count, " times")