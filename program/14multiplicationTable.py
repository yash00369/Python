#Multiplication Table  with for loop
num=int(input('Enter a number:'))
for i in range(1,10+1):
  print( num,'x',i, "=",num * i)

#Multiplication Table  with while loop 

num=int(input('Enter a number:'))
i=1
while i<=10:
  
  print( num,'x',i, "=",num * i)
  i+=1

