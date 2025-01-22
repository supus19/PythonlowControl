my_number = input("enter a number: ")
try:
    my_number = int(my_number)
    print(my_number, 'is a fun number')
except:
    print("Please enter a number")
    print(my_number, 'is not a number')

print('done')