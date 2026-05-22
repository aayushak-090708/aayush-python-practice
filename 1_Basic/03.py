print("this is a calculater and press enter after each number you write")
a=int(input("enter first number"))
c=input("enter a maths operator")
b=int(input("enter second number"))
if c=="+":
 print(a+b)
elif c=="-":
 print(a-b)
elif c=="/":
 print(a/b)
elif c=="*":
 print(a*b)
else:
 print("wrong operator")