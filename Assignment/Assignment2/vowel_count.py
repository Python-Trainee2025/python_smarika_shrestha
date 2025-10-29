# 2. Accept a word/sentence from the user and
# count how many vowels (a, e, i, o, u) are present in it.

sentence=input('enter your sentence:').lower()

character=list(sentence)

vowel=['a','e','i','o','u']

for v in vowel:
    count=character.count(v)
    print(f'{v} appears {count} times')

