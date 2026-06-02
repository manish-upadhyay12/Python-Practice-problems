#  Find the greatest element and print its index.
# solve this question using  two approach

input = [4, 8, 2, 9, 1, 1, 2, 3, 10]
max = input[0]  # fix fist element max and check according to first element
index = 0
print("This is first approach to find max using index :")
for i in range(0, len(input)):

    if input[i] > max:
        max = input[i]
        index = i

print(max)
print(index)


# second apporach to solve this :
for i in range(0, len(input)-1):
    for j in range(i+1, len(input)):
        # Input.sort()

        if input[i] < input[j]:
            if input[j] > max:
                max = input[j]
                index = j
print("this is second approach to find max ")
print(max)
print(index)
