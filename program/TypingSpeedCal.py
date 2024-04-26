from time import *
import random as r

def  mistake(partest,usertest):
  error=0
  for i in range(len(partest)):
    try:
      if partest[i] !=  usertest[i]:
        error=error+1
    except:
      error=error+1    
  return error

def speed_time(time_start,time_end,userinput):
      time_delay=time_end -time_start
      time_R = round(time_delay,2)
      speed = len(userinput)/time_R
      return round(speed)
while True:
  ck=input("ready to test: yes/no: ")
  if ck=="yes":   
     test =["Python is a multipurpose, high-level, object-oriented programming language","three properties that make it popular with coders and developers. "]
     test1= r.choice(test)
     print("   *******  typing speed  ******* ")
     print(test1)
     print()
     print()
     print()


     time_1=time()
     testinput=input('Enter: ')
     time_2=time()


     print('Speed:',speed_time(time_1,time_2,testinput),"w/sec")

     print("error",mistake(test1,testinput))

  elif ck=="no":
     print("thank you")
  else:
     print("wrong input")  
  
      






   