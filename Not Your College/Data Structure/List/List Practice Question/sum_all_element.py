# Question : take input from user and print sum of all element
  # and average also 
l = []  # blank list
sum = 0
range_of_list = int(input("enter range of element"))
for i in range(0, range_of_list):
    element = int(input(f"enter {i+1} number:"))  # Take input
    l.append(element)  # add in list
    sum += l[i]
  
average = sum//range_of_list
print(f"Average of lis is {average}")
print("sum of all element ", sum)
