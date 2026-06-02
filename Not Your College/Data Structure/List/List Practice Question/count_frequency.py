# Question : count max frequency number
l = [1, 1, 1, 4, 4, 5, 5, 8, 8, 81, 1, 4, 7, 7, 8, 1, 1, 1, 1]

l.sort()
print(l)
se = set(l)
print(se)

count = 0
for i in range(0, len(l)-1):
    if l[i] == l[i+1]:
        count += 1
    if l[i] != l[i+1]:
        print(f"element {l[i]} : frequency {count+1}")
        count = 0
