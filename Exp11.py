n1= eval(input("Enter 1st no.: "))
n2= eval(input("Enter 2nd no.: "))
#To fing GCD of two numbers
for i in range(min(n1,n2), 0,-1):
    if (n1%i==0 and n2%i==0):
        gcd=i
        break
print("GCD of ",n1," and ",n2," is: ",gcd)