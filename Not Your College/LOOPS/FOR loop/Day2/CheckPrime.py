# Question : check a number is a prime or not
n= int(input("enter number to check is it prime or not :"))
for i in range(2,n):
    if(n%i==0):
        print("not a prime number ")
        break
else:
    print("prime number")