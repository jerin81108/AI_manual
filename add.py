n=int(input())
count=0
no=0
for i in range(1,n):
   if i%2==0:
      count=count+i
   if i%2!=0:
      no=no+i
print('sum of even=',count)
print('sum of odd=',no)
