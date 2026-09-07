n=int(input())
for i in range(0,n,2):
    print(' '*(n-i),end="")
    c=1
    for j in range(i+1):
        print(' *',end='')
        c=c*(i-j)//(j+1)
    print()

l=int(input())
for k in range(1,l,2):
    print('*'*k)
