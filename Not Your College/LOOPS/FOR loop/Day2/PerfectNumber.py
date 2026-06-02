# Question : check if a number is a perfect number

n = int(input("enter number for checking is it perfect no. :"))

sum = 0
for i in range(1,n):
    if( n%i==0):
        sum= sum+i

if sum== n :
    print("This is a perfect number")
else:
    print("This is not a perfect number")