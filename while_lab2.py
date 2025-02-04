print("Starting While Loop - Print Count Variable")
x = 0
while x <10:
    print(x)
    x+=1
print("Ending While Loop")

print("Starting Coding Challenge")
while True:
    try:
        x = int(input("Input a number from 0 to 9: "))
    except:
        print("Invalid input. Please enter a whole number")
    else:
        print(x)
        print("Starting While Loop - Comparing User & Counter")
        break
y = 0
while y <10:
    print(y)
    y+=1
    if y == x:
        print("User Variable is equal to Count Variable")
        print("User = ", x)
        print("Count = ", y)
        continue

