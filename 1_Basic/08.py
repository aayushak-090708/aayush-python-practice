print("this code prints all prime numbers from 1 to 50")
for i in range (1,51):
 if i>1:
  for j in range (2,i):
   if i%2==0:
    break
  else :
   print(i)