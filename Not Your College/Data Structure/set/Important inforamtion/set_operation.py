 # under stand set operation

# difference (-)  = remove common element
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print("difference ",s2-s1)  # (-) also used to remove common element
print("difference ",s1.difference(s2))   #method to remove common element form s1
print("difference ",s2.difference(s1))  #method to remove common element form s2

# difference_update(-=) = we can also save remove save element we can not pront directly
s1 = {10,20,30,40}
s2 = {30,40,50,60}
#print(s2-s1) # output : {50,60}
#s2-=s1   # common element remove and update set
s1.difference_update(s2)
s2.difference_update(s1)
print("difference_update ",s1)
print("difference_update ",s2)

# intersection(&)   = return commonvalue 
s1 = {10,20,30,40}
s2 = {30,40,50,60}
print("itersection :",s1 &s2)

#intersection_update(&=)  = update set and return commmmon value of specific set
s1 = {10,20,30,40}
s2 = {30,40,50,60}
s1 &=s2
print("intersection_update :",s1)

# issubset(<=) = return true if subset is present in set
s1 = {10,20,30,40}
s2 = {30,40}
print("issubset :",s2<=s1)
# print("subset : ",s2.issubset(s1))

# issuperset(>=)
s1 = {10,20,30,40}
s2 = {30,40,54}
print("issuperset : ",s1>=s2)