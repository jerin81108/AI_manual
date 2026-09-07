def amst():
    n=int(input('enter a number'))
    sum=0
    x=n
    f=str(n)
    l=len(f)

    while x>0:
        d=x%10
        sum+=d**l
        x//=10
        
    if sum==n:
        return 'amstrong number'
    else:
        return 'not a amstrong number'

a=amst()
print(a)