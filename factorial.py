def fact(n):
  if n==1:
    return 1
  else:
    res=1
    for i in range(1,n+1):
      res*=i
    return res

num=int(input("Enter the number:"))
print(fact(num))
