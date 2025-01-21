def main():
    print("Starting The Code Challenge")
    x=12
    if x>9:
        print("The if statement was evaluated as True")

    x = 12
    if x > 9 :
        print("x is equal to or greater than 10")

    x = 12
    y = 8
    if x >= y :
        print(x, "is equal to or greater than ", y)

    x = input("Enter a number > ")
    y = 8
    if int(x) >= y :
        print(x, "is equal to or greater than", y)
    print('Done')


    x = input("Enter a number > ")
    x = int(x)
    y = 8


    if x >= y :
        print(x, "is equal to or greater than", y)
    else :
        print(x, "is less than", y)

    print('Done')

    x = input("Enter a number > ")
    x = int(x)
    y = 8


    if x > y :
        print(x, "is greater than", y)
    elif x == y:
        print(x, "is equal to ", y)
    else :
        print(x, "is less than ", y)
    print('Done')


    print("Ending The Code Challenge")

main()