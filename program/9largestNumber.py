#check number is largest amoungst three number

num1=float(input('Enter number here:'))
num2=float(input('Enter number here:'))
num3=float(input('Enter number here:'))

if (num1>num2)&(num1>num3):
  print(num1 ,'is Larger')
elif(num2>num1)&(num2>num3):
  print(num2 ,'is Larger')
else:
   print(num3 ,'is Larger')
