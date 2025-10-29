# 5. Read a .csv file and print each row. Handle file not found and other parsing errors if needed

import csv

sample_data = [
    ['Ram', '30'],
    ['Shyam', '25'],
    ['Hari', '35']
]

with open('file2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)

try:
    with open('file2.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print('file not found')

