windows_are_dirty = 5
while windows_are_dirty > 0:
    print("Wipe On")
    print("Wipe Off")
    windows_are_dirty -= 1
print("Windows are clean")

n = 5
print('Say Cheese...')
while n>0:
    print(n)
    n = n-1
print("Click!")

while True:
    line = input('>')
    if line == 'done':
        break
    print(line)
print("Done")


while True:
    line = input('>')
    if line[0] =="#":
        continue
    if line == 'done':
        break
    print(line)
print("Done")


x=5
y=3
while True:
    print('x=',x,'\ny=',y)
    z=x+y
    print('x+y=',z)
    if (z==8):
        break
    x+=1
    print("y is still", y, 'but x is now', x)
print('Done')