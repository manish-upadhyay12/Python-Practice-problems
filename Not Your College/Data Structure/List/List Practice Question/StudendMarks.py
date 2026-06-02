# Question : take 6 student marks and print them in sorted manner 

for j in range(1, 7):
    marks = []

    print(f"enter {j}  student")
    for i in range(1, 7):
        m = int(input(f"  marks of {i} subject :"))
        marks.append(m)
    marks.sort()
    print(marks)





