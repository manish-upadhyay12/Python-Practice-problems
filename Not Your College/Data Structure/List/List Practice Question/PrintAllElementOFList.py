# Question : print all positive and negative element seperatly
# using index method and direct value method

input = [3, -1, 4, -5, 9, 1, -5, 9, -4, 8, 7, -5]
positive = []  # empty list
negative = []  # wmpty list

# 1st approach usingindex
positive = []
negative = []
for i in range(0, len(input)):
    if (input[i] >= 0):              # check positive
        # append only add value in last here append is not working on index
        positive.append(input[i])
    elif (input[i] < 0):             # check negative
        negative.append(input[i])

print(positive)          # print positive list
print(negative)          # print negative list


# # second approach using list only
# pos = []
# neg = []
# for i in  Input:
#     if(i>=0):              # check positive
#        pos.append(i)  # append only add value in last here append is not working on index
#     elif(i<0):             # check negative
#         neg.append(i)

# print(pos)
# print(neg)
