# Question : check number  is a palidrome number or not

n = int(input("enter number :"))
123
rev =0
tem = n
while(n>0):
    rev = rev*10 +(n%10)
    n= n//10

if tem == rev:
 print(f"{tem} is a palidrome number")

else:
   print(f"{tem}is not a palidrome number")