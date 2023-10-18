import collections

student = collections.namedtuple('student',['name','age','peso'])

s1  = student("Alex",18,65)
print(s1.name)
print(s1.age)
print(s1.peso)

print(s1[0])
print(s1[1])
