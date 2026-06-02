# Question : take input from user student name,marks and find print all and decide
            #  grade according to percent and also find average of marks

name = input("enter you good name :")
marks = []  # blank list
sum = 0
for i in range(0, 5):
    mar = int(input(f"subject {i+1} marks :"))
    marks.append(mar)
    sum += marks[i]

percent = (sum/500)*100   # find percent

# position decide
if percent >= 90:
    print("1st position ,very good")

elif (percent >= 80 and percent < 90):
    print("2nd  position ,good ")

elif (percent > 30 and percent < 80):
    print(" 3rd position, try next time  ")

else:
    print("fail")

average = sum/5  # find average 
print(f"name of student is {name}")   # print name of student
print(f"marks of student {marks}")    # print marks of student
print(f"Average of all subject {average}")  # print average of all marks
