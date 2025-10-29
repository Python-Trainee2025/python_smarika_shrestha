#ASSIGNMENT 1

# 1. Take input from user for two words, and check if they are anagrams
# (angram example: listen and silent -> both contain the same number and set of alphabets)

word1,word2= input("enter two words separated by comma:").split(',')

list1=list(word1.lower().strip())
list2=list(word2.lower().strip)
list1.sort()
list2.sort()

if list1==list2:
    print("The words are anagram")
else:
    print("The words are not anagram")
