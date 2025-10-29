# 3. Input a sentence or a paragraph from user and extract how many unique words are used and display the count

sentence=input("Enter a sentence: ").lower().strip().split(' ')

distinct_words=list(set(sentence))

for i in distinct_words:
    print(i)
    count=sentence.count(i)
    print(f"The count of {i} is {count}")