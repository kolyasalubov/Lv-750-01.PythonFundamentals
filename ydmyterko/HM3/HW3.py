x = 1
y = 2

#solution 1
print("Init x:", x)
print("Init y:", y)

x = x+y
y = x-y
x = x-y
print("Swap x:", x)
print("Swap y:", y)

#solution #2
x = 1
y = 2
print("Init x:", x)
print("Init y:", y)

x,y = y,x
print("Swap x:", x)
print("Swap y:", y)