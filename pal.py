n=121
r=0
x=n
while x:
    r=r*10+x%10
    x//=10
print('palindrome'if r==n else'not a palindrome')