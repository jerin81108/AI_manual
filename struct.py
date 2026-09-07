students={}#dictionary &its operation
students['name']=input('enter a name')
print(students)
student={'name':'ananiya','age':3,'shl':'kg'}
print(student)
print(student.get('name','invalid entry'))
print(student.keys())
print(student.items())
student.update({'name':'ananya','age':4,'shl':'kinder'})
print(student)