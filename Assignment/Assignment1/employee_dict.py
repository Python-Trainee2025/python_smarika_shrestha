# 4. Create a dictionary with a person's name and contact info for a small company,
# take the input from a user to search for a user using their name, return the number
# (example user will search for 'Ram' and if user exists, their phone number is returned)

dict={
    'person1': {'name':'Ram', 'contact': 9812345678},
    'person2': {'name':'Shyam', 'contact': 9834123456},
    'person3': {'name':'Mohan', 'contact': 9812345699}
}

name=input("Enter the name who's contact number you require:")

found=False
for i in dict:
    if dict[i]['name']==name:
        print(f"{dict[i]['name']}'s contact number is {dict[i]['contact']}")
        found=True
        break

if not found:
        print("User does not exist")