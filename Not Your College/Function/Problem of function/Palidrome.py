# Question :check number is a palidrome number or not using function


def palidrome_number(n):
    rev = 0
    tem = n

    while (n>0):
        rev = rev*10 +(n%10)
        n=n//10
        
    if tem == rev:
       print(f"{tem} is a palidrome number")
    else:
      print(f"{tem} is not a palidrome number")
 

number = int(input("enter number :"))
nu = int(input("enter number :"))
num = int(input("enter number :"))
numb = int(input("enter number :"))
palidrome_number(number)
palidrome_number(nu)
palidrome_number(num)
palidrome_number(numb)