# Question : check  list is sorted or not if unsorted then sorted

l = [2, 51, 5, 7, 9, 4, 7]

for i in range(0, len(l)-1):   # This loop check list is sorted or not
    if l[i] > l[i+1]:
        # if list is unsorted print unsort and break
        print("list is unsorted", l)
        break
else:
    print("List is sorted no need to sort")

for i in range(0, len(l)-1):
    for j in range(0, len(l)-1):
        # These both loop sort the list
        tem = l[j]
        if l[j] > l[j+1]:
            l[j] = l[j+1]
            l[j+1] = tem

print("sorted list are : ", l)
