# swapTwoVariable using third variable
x=12
print(x)
y=13
print(y)
temp=x
x=y
y=temp
print("value of x after swaping: ", x)
print("value of y after swaping:",y)


#with out third variable
x=32
y=33
x,y=y,x
print("value of x after swaping: ", x)
print("value of y after swaping:",y)