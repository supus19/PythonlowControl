# Python Lab - Introduction to "IF" statements
print('''
This Lab is about the 'IF' statement and how we ask questions.

Hint: Check out W3Schools IF
- https://www.w3schools.com/python/python_conditions.asp
      ''')
x = 12  # Don't change this value
if x > 9 :
  print("x =",x)
  print("The 'if' statement x > 9 was evaluated as 'True'")

# Challenge 1
# Write and play with "IF"
print('''
Challenge # 1
----------------------------------------------------
Run this code, review it, and then change the comparison operation.
      
Ways to compare objects
      
x == y      # x is equal to y
x != y      # x is not equal to y
x > y       # x is greater than y
x < y       # x is less than y
x >= y      # x is greater than or equal to y
x <= y      # x is less than or equal to y
x is y      # x is the same as y
x is not y  # x is not the same as y      

# If you change the comparison operation, remember to change 
it in the print statment too
---
''')
# -------------------------------------------------
print('''Answer to Challenge 1
# If you change the comparison operation, remember to change 
it in the print statment too
-------------------------------------------------''')
x = 6
y = 9
z = 12
print("x =",x)
print("y =",y)
print("z =",z)
if x < y : 
  print("The if statement",x,"<",y,"was evaluated as 'True'")

if x > z : 
  print("The if statement",x,">",z,"was evaluated as 'True'")

if x == z : 
  print("The if statement",x,"==",z,"was evaluated as 'True'")

if x == y-4 : 
  print("The if statement",x,"==",y-4,"was evaluated as 'True'")
print('''
Add 3-4 more of your own if statements
-------------------------------------------------''')

if x<= y:
  print("Apples are samller than oranges")

if x != y:
  print("Tomatoes are not vegetables")

if x>=y:
  print(x+y)