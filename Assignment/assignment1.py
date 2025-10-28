#ASSIGNMENT 1

# 1. Take input from user for two words, and check if they are anagrams
# (angram example: listen and silent -> both contain the same number and set of alphabets)

# word1,word2= input("enter two words separated by comma:").split(',')
#
# list1=list(word1.lower())
# list2=list(word2.lower())
# list1.sort()
# list2.sort()
#
# if list1==list2:
#     print("The words are anagram")
# else:
#     print("The words are not anagram")

# 2. Get input from user and check if it is palindrome

# word=input("enter a word: ").lower()
# reversed_word=word[::-1]
#
# if word==reversed_word:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

# 3. Input a sentence or a paragraph from user and extract how many unique words are used and display the count

# sentence=input("Enter a sentence: ").lower().split(' ')
#
# distinct_words=list(set(sentence))
#
# for i in distinct_words:
#     print(i)
#     count=sentence.count(i)
#     print(f"The count of {i} is {count}")

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




