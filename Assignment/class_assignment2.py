#check whether a prime number or not

num=int(input("enter a number:"))
count=0

for i in range(2,num):
    if num%i==0:
        count+=1
        break

if count==0:
    print('prime')
else:
    print('not prime')



# num=int(input("Enter a number: "))
#
# result=True
#
# if num<=3:
#     result=True
# else:
#     for i in range(2,num):
#         if num%i==0:
#             result=False
#             break
#
# if result==True:
#     print("The number is prime.")
# else:
#     print("The number is not prime.")





