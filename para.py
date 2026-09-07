def add(a,b):   #def using parameter
    print(a+b)
add(33,47)

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

add(5,2)
sub(5,2)
mul(3,4)
div(5,10)

def oe(a): 
    if a%2==0:
        print('it is even')
    else:
        print('it is odd')
oe(7)

def pf(a):
    if a<=34:
        print('fail')
    else:
        print('pass')
pf(77)

def rng(a,b):
    for i in range(a,b):
        print(i,end='')
rng(1,10)