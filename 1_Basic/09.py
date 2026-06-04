#roman to decimal converter

a=input("Enter a roman numeral: ")
a=a.upper()
l=list(a)
l=l[::-1]
d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
t=0

for i in range(len(l)):
    if i==0:
        t+=d[l[i]]
    else:
        if d[l[i]]>=d[l[i-1]]:
            t+=d[l[i]]
        else:
            t-=d[l[i]]
print("The decimal value is: ",t)





  