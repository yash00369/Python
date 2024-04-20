num=int(input('enter a  three digit number  :'))
order=len(str(num))

sum=0
temp=num
while temp>0:
  digit=temp%10
  cube=digit**order
  sum=sum+cube
  temp//=10 #remove digit after point(.) we use floordivision(//).

if sum==num:
  print('it is an armstrong number')  
else:
  print('it is not an armstrong number')  