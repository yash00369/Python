# Sum of natural number
num=int(input('Enter a number here:'))
if num<0:
  print('Please enter postive number')
else:
  sum=0
  while num>0:
      sum +=num
      num -=1
      print(sum)