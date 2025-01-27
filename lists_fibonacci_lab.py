print('''LISTS - Assigning values by using Append, Extend, Concatenate
Learn more about Lists here:
https://www.w3schools.com/python/python_lists.asp
''')      
print('''
Challenge #1 Fibonacci
Run, then Edit the code in the template example:
      
fibonacci_sequence = [0,1,1,2,3, 5, 8, 13, 21, 34]
Rather than just creating the list with the number, 
write a program to calculate the fibonacci number and then 
append, extend and concatenate the sequence
- See how the append works with fibonacci_sequence[0]+
  fibonacci_sequence[1]
- Do this again to append the next value in the sequence.
- Write a for loop to calcualte and .append 10 more 
  numbers in the sequence
- Write a for loop to calcualte and .extend 10 more 
  numbers in the sequence
      ''')

fibonacci_sequence = [0,1]
print(fibonacci_sequence)

# .append method to Appending to the list
fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
print(fibonacci_sequence)

# Use the .append to add the next number in the sequence.
fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
print(fibonacci_sequence)

# Use a for loop to calculate and .append 10 more of the next numbers in the sequence
for _ in range(10):
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
print(fibonacci_sequence)

# Use a for loop to calculate and .extend 10 more of the next numbers in the sequence
new_fib_numbers = []
for _ in range(10):
    new_fib_numbers.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
fibonacci_sequence.extend(new_fib_numbers)

print(fibonacci_sequence)
