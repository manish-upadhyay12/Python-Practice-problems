# Question : print sum of even and odd number separately

n = int(input("enter n range :"))

evenSum  = 0  # store even value
oddSum  = 0   # store odd value
for i in range(1,n+1):
    if (i%2==0):
        evenSum= evenSum +i
    else:
        oddSum = oddSum+i

print("even sum is :",evenSum)
print("odd sum is :",oddSum)