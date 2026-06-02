# Question : find the factorial 

fa = int(input("tell number to find factorial :"))
product = 1
for i in range(fa,1,-1):
    product = product*i

print(product)