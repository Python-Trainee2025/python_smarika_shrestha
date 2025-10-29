#1. Write a program that takes a number n and prints the first n numbers in the Fibonacci sequence.
# Use both Recursion and regular method

#Regular method
# num=int(input('enter the number of terms: '))
#
# def fib(n):
#     a=0
#     b=1
#     for i in range(1,n+1):
#         if n==1:
#             print(a)
#             break
#         print(a)
#         c=a+b
#         a=b
#         b=c
#
# fib(num)


# Recursive function to generate Fibonacci numbers
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num=int(input("Enter the number of terms: "))
for i in range(1, num+ 1):
    print(fibonacci(i))






