n=int(input('enter a value:'))
m=int(input('enter a range:'))
count=0
no=0
for i in range(n,m):
   if i%2==0:
      count=count+1
   if i%2!=0:
      no=no+1
print('no of iteration of even=',count)
print('no of odd no in iteration=',no)
