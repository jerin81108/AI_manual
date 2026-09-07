a='AIDS'#user id
p='2ndyear'#password
b=input('enter the user name:')
c=input('enter your password:')

def validate():
    if a==b and p==c:
        return 'True'
    else:
        return 'False'
d=validate()
print(d)