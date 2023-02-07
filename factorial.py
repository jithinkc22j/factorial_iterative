#Program to find the factorial of a number using iterative method
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
    
print("Factorial of a number \n")
n=int(input('Enter your number:'))
for i in range(1,n+1):
    s=fact(i)
print('The factorial of a number',n,'is',s)
