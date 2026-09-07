def oe():  #def function without parameter
    a=int(input('enter a number'))
    if a%2==0:
        print(a,' is even')
    else:
        print(a,'is odd')



def pf():
    n=int(input('enter your mark'))
    if n<=34:
        print('improve your studies')
    else:
        print('you are succeeded')



def rng():
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    for i in range(a,b):
        print(i,end='')
oe()
pf()
rng()