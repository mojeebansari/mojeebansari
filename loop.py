#i = 0
#while i < 5:
   # i=i+1
  #  print(i, i*"*","im mojeeb",i*"*")
  #  break
    
import random
    
guess=random.randint(1,9)
tr = 4
 
while tr>0:
 inp = int (input("guess the number from 1 to 9     "))    
 if inp==guess:    
     print("you won")  
     print("tries left", tr-1)
     break
 else:    
     tr=tr-1    
     print("tries left =" , tr)
     if tr == 0:
         print("you lost the chances")
    
     
    
   
       