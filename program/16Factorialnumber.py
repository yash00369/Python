# Factorial with for loop

# num=int(input('enter a number to obtain factorial :'))
# factorial=1

# if num<0:
#   print("factorial of 0  doesn't exist")
# if num==0:
#   print("factorial of 0 is :",1)  
# if num>0:  
#   for i in range(1,num+1):
#     factorial =factorial*i
#     print('the factorial of given number is : ',factorial)




# Factorial with recursion
num=int(input('enter a number to obtain factorial :'))
def fact(a):
  if a==0:
    return 1
  else:
    return a*fact(a-1)

result=fact(num)
print('factorial of given number:',result)
  
