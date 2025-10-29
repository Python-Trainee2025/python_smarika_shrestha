# 2. Get input from user and check if it is palindrome

word=input("enter a word: ").lower()
reversed_word=word[::-1]

if word==reversed_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
