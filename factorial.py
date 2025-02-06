def fact(n):
  if n==1:
    return 1
  else:
    res=1
    for i in range(n,n+1):
      res*=n-1
    return res

num=int(input("Enter the number:"))
print(fact(num))
