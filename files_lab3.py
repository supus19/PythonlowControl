# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and reading 
the file, line by line using the file method: 
- file_handle = open(file_name) method
      ''')
# Challenges
print('''
Challenge #1 & #2
----------------------------------------------------
#1 - Edit the code below to count each line, 
     and print the total out at the end
      
#2 - Edit the code below to open the text-file-mail-short.txt file
---
''')
# -------------------------------------------------
print('''Answer to Challenges
-------------------------------------------------''')

# Open the file and initialize the line count variable
count = 0
with open('text-file-mail-short.txt') as fhand:
    for line in fhand:
        count += 1  # Increment the line count variable
        print(line.strip())  # Print the line without extra newlines

print('Line Count:', count)
print('''
-------------------------------------------------''')