# '''
# when we write variable name in all cap it acts like a constant
# pi=3.14 is a variable
# PI=3.14 is a constant
#
# we do not need to define the variable type like string , int
#
# '''
#
# #type casting
# #types: implicit and explicit type casting
# c='15'
#
#
# print(type(c))
# print(type(int(c)))
#
#
# # input
# i=input("enter number")
# print(type(int(i)))
#
# #output types
# name="Ram"
# age=30
#
# print("Name is {} and Age is {}".format(name,age))
# print(f"Name is {name} and Age is {age}")

#string manipulation
# r='car'
# t='apple'
# p='race'
#
# print(p+r) #concatenation
# print(p*4) #repitation
# print(p[0]) #indexing
# print(t[1:3]) #slicing[start:end] includes start but not the end
#
# print(t[::-1]) #reverse string
#
#
# print('b' in t) #membership test
# print('b' not in t) #membership test
# print(len(t))

# a='apple pie'
# print(a.lower())
# print(a.upper())
# print(a.title()) #first letter of all word
# print(a.capitalize()) #first letter of first word only
#
# z='       apple'
# print(z)
# print(z.strip()) #removes whitespace
# print(z.replace('p','q'))

b='hello my name is ram'
s=b.split(" ") #split words based on values
print(s)

j=" ".join(s)
print(j)

a='apple'

print(a.startswith('a'))
print(a.endswith('e'))
print(a.isalpha())
print(a.count('p'))

