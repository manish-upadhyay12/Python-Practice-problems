 # Question : find the factore of number'

n = int(input("enter number for counting factor :"))
factoreCount = 0
for i in range(1,n+1):
    if n%i==0:
        factoreCount = factoreCount +1

print("factor of a number is:",factoreCount)

