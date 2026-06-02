# Question : find the second largest element in list
input = [1, 5, 8, 7, 9, 6, 5, 10, 7, 4, 1, 2, 5]
max = input[0]
secondMax = input[1]
secondMax = 0
index = 0

for i in range(1, len(input)):
    if (input[i] > max):
        max = input[i]
        index = i

# print(f"first max number is {max}  and index of first max is {index}")
SecondMax = input[0]
for i in range(1, len(input)):  # max = 10
    if (input[i] > secondMax and input[i] != max):
        secondMax = input[i]
        index =i
     
print(f"second max is {secondMax}  and index of second max is { index}")   


