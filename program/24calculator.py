print('Mini Calculator')
a=float(input('Enter a number :'))
b=float(input('Enter a number :'))

print('Press 1 for addition \n Press 2 for substraction \nPress 3 for multiplication \nPress 4 for division ')

choice=int(input('Enter your choice:'))
if choice== 1:
  print(a+b)

elif(choice==2):
  print(a-b)
elif(choice==3):
  print(a*b)
elif(choice==4):
  print(a/b)    
else:
  print('invalid choice you enter')