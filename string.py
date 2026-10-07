name = "Alan Mathews"

course = 'Python Programming'

address ="""
Kottyam
Kerala
India
"""

# type casting-changing datatype

# rno = str(6)

# print (name,course,address)
# print(type(name))
# print(len(name))
# print(len(address))

# print (name[0])
# print(course[5])

# slice start,end,step/skip

# print(name[0:5])
# print(course[5:16])
# print(course[2:10:2])
# print(course[0:17:3])

# print(name[-1])

# print(course[-10:-1])
# print(course[-10:-1:2])
# print(course[:5])
# print(course[5])
# print(course[4:])
# print(course[:: 2])
# print(course[::-1])


# string modules


print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.swapcase())

print(name.startswith('Ala'))
print(name.endswith('ews'))
print(name.isalpha)
print(name.isdigit)
print(name.isalnum)
print(name.strip()+'dfdfdf')
print(name.lstrip()+'qwe')
print(name.rstrip()+'rerwe')

print(name.split(' '))
print(name.split('c'))

print('*'*8)
print("A is" ,14,", which is greater than 100 :" ,14>100)
print(f"\n\nA is {14} ,\t which is greater than 100: {14>100}")