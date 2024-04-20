# using lambda function and filter()

l=[39,48,98,26,67,87]
result=list(filter(lambda x : x % 13==0,l))
print('the number is divisible by 13 is:',result)