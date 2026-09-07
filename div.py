n=int(input('enter a number :'))
count=0
for i in range(1,n):
    if i%3==0 and i%5==0:
        count=count+1
print(count)
