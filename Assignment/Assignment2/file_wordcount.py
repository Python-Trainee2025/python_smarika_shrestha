#3. Read a text file and count the number of words in it.
# Handle the case where the file might not exist.

with open('file1.txt','w') as file:
    file.write('hello world i am apple apple i w q e r  ')

try:
    with open('file1.txt','r') as file1:
        fileData=file1.read().strip()
        listOfFileData=fileData.split(' ')
        print(listOfFileData)
        wordCount=len(listOfFileData)
        print(f'The word count of the file is {wordCount}')
except FileNotFoundError:
    print('File not found')

