def gcd(a,b):
    n=min(a,b)
    gcd=0
    for i in range(1,n+1):
        if a%i==0 and b%i==0:
            gcd=i
    print("GCD is:",gcd)

num1 = int(input("Enter the 1st number:"))
num2 =int(input("Enter the 2nd number:"))
gcd(num1,num2)


