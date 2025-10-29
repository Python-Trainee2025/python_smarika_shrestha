# input income amount and tax rate in one line, calculate total as income * tax and display

# ip=input('Enter the income and tax separated by comma:').split(',')
# income=int(ip[0])
# tax=int(ip[1])
# total= income-(income*tax)/100
# print(f"The total is {total} for income {income} and tax {tax}")

#the data is initially inputed as string in the list
#type casting each of the element of the list is not feasible so we can directly map it

ip=list(map(int,input('Enter the income and tax separated by comma:').split(',')))

total=ip[0] - (ip[0]* ip[1]) /100

print(f"The total is {total} for income {ip[0]} and tax {ip[1]}")