#display power of 2 as anonymous function

nterms=int(input('enter number of terms here:'))
result=list(map(lambda x:2**x,range(nterms+1)))
print(result)

