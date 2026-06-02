 # Question : check how many char ,digit,number in a string
# str.isdigit(),str.isalpha
n  = "p!@yn26at^&i5vw"
char = 0
specialCharcter = 0
digit = 0


for i in n:
  
    if (ord(i)>=65 and ord(i)<=90) or(ord(i)>=97 and ord(i)<=122):
     char+=1
    elif (ord(i)>=48 and ord(i)<=57):
       digit+=1
    else:
       specialCharcter+=1
print(f"char -{char},specialChar -{specialCharcter},digit-{digit}")
