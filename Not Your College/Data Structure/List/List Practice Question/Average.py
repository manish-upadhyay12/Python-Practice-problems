 #  Find the mean (average) of all list elements.

input= [10, 20, 30, 40]
sum = 0   
length = len(input)
for i in input:
    sum+=i

average = sum/length # formula to find average 
print("Average of all list element is :",average)