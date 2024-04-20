a=int(input('Enter a number :'))
b=int(input('Enter a number :'))
def calHCF(x,y):
  if x>y:
    smaller=y
  else:
    smaller=x  
 
  for i in range(1,smaller+1):
    if((x%i==0)&(y%i==0)):
      hcf=i
  return hcf
print('the HCF of given number is',calHCF(a,b))  
