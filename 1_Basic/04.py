def compound_interest(principal, rate, time, n=1):
    amount = principal * (1 + rate/n)**(n*time)
    return round(amount, 2)

P = int(input("enter principal:"))   
R = int(input("enter annual interest:"))    
T = int(input("enter time:"))    
print("Final Amount:", compound_interest(P, R, T))