n=str(input('enter your name:'))
b=int(input('enter your mark sub1:'))
c=int(input('enter your mark sub2:'))
d=int(input('enter your mark sub3:'))
e=int(input('enter your mark sub4:'))
f=int(input('enter your mark sub5:'))
g=b+c+d+e+f
a=g/5
print('total mark:',g)
print('average:',a)
if a>=90:
    print(n,'your grade is A')
elif a>80:
    print(n,'your grade is B')
elif a>70:
    print(n,'your grade is C')
elif a>50:
    print(n,'your grade is D')
else:
    print(n,'improve your studies')