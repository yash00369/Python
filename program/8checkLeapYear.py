# Check year is leap Year or not

year=int(input('Enter a year:'))
if (year %400==0) & (year %100==0):
  print(year,'Is a leap year')
elif (year%4==0) &(year % 100!=0):
   print(year,'Is a leap year')
else:
   print(year,'Is not a  leap year') 
