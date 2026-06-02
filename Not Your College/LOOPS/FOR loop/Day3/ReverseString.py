# Question : reverse a string without using built function


# print(n[::-1])   # this is a function we cannot use in this


n = input("enter string to reverse :")
reverse =""
for i in range(len(n)-1,-1,-1) :  # -1 = 0,len() = last index
   reverse = reverse+ n[i] +" "

print(reverse)  # print reverse string