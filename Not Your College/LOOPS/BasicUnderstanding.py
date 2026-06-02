  # Question : print table of 5

# for var in range(5,50,5):
# #     print(var)
#  # for string 


a = "manish"
for i in range(len(a)):  #for string 
    print(f"{i} : {a[i] }")

for i in range(len(a)):
          print(a[i])


n = int(input("enter your number:"))
a = 1
for i in range(n,(n*10)+1,n):
      print(f"{n} *{a} = {i}")# formated string 
      a=a+1  # updation  of a 