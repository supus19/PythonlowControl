# Opening File Handles and reading data from files
print('''
This Lab is about opening a file handle, and 
printing the file handle.

Hint: Check out W3Schools File Handling
- https://www.w3schools.com/python/python_file_handling.asp
      ''')
# -----------------------------
print('''
Challenge
----------------------------------------------------

What happends if the file does not exist? 
- Try opening a file that does not exist... 
Like "matrix2.txt"

Can you open a diffrent file? 
- Try opening the file "mbox-short.txt"
---
''')
# -------------------------------------------------
print('''Answer to Challenge:
      If file does not exist, it gives error: no such file found in directory.
      You can open the file as long as it exist in the directory. ''')
# Try opening a file that does not exist... Like "matrix2.txt"
xfile = open('matrix.txt')
print(xfile)
print('''
-------------------------------------------------''')