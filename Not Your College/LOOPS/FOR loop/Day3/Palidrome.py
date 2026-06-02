# Question : check string is a palidrome number or not

n = input("enter string to check palidrome or not:")

reverse = ""
for i in range(len(n)-1,-1,-1):
    reverse = reverse +n[i]

if reverse == n :
    print("String is a palidrome ")

else:
    print("String is not palidrome")    
