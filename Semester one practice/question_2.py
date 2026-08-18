#i,a
x=int(input("Enter a value"))
y=int(input("Enter a value"))
x,y=y,x
print("x=", x, "y=",y)
#i,b
x=int(input("Enter a value"))
y=int(input("Enter a value"))
x=x+y
y=x-y
x=x-y
print("x=", x, "y=",y)
#ii
x=int(input("Enter a value"))
y=int(input("Enter a value"))
temp=x
x=y
y=temp
print("x=", x, "y=",y)