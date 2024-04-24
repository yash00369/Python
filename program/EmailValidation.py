# email validation using string5
email=input("enter your Email: ")
k,j,d=0,0,0
if len(email)>=6:
  
   if email[0].isalpha():
      
      if ("@" in email )& (email.count("@")==1):
         if (email[-4]==".") ^ (email[-3]=="."): # we use xor operator ,in which one condition is true afterthat it return true otherwise it return false.
            for i in  email:
                if i==i.isspace():
                  k=1
                elif i.isalpha():
                  if i==i.upper():
                     j=1
                elif i.isdigit():
                   continue
                elif i=="_" or i== "." or i=="@":
                   continue
                else:
                   d=1  
                        
            if k==1 or j==1 or d==1:
               print('invalid email')     
            else:
               print("right Email")    

            
      
         
         else:
            print('invalid email . is missing')
      else:
         print("invalid Email @ is missing")




   else:
      print('invalid Email first letter will be alphabate ')

else:
  print('wrong Email too short email')




# Email validation using regEx
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email:")
if re.search(email_condition,user_email):
   print('Right Email')
else:
   print("Wrong Email")   