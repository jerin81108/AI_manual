def fact(n):
    return 1 if n==0 else n*fact(n-1)
print(fact(5))


n=int(input('enter a number:'))
fact=1

for i in range (1,n+1):
    fact=fact*i

print(fact)