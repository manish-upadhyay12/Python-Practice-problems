# Question : print natural number 1 to n

n  = int(input("enter your number :"))
a = 1
for ma in range(1,n+1):
    if (ma%10==0):  # condition for if ma is divisible of 10 continue run
    # a=a+10
     continue  
    print(ma)