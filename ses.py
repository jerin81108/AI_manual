
a=int(input('enter the time in 24 hours format:'))
if (a>19 and a<=24) or (a<4 and a>0) :
    print('it is night')
elif a>4 and a<12:
    print("it is morning")
elif a>12 and a<15:
    print('it is noon')
elif a>15 and a<19:
    print('it is evening')
else:
    print('invalid number or not a time')