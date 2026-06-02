# Question: reverse list and orginal list

l = [10, 20, 45, 54, 89, 47, 45, 78, 98, 74, 85, 78, 95]
print(f"orginal list {l}")
start = 0  # starting point
end = len(l)-1   # ending point

while (start < end):  # condition when start is less than end
    tem = l[start]    # tem = store starting value
    l[start] = l[end]
    l[end] = tem
    start += 1
    end -= 1

print(f"reverse list {l}")
