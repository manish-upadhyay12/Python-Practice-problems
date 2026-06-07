 # 
# convert list to set
l = [10,2,30,40]
s  = set(l)
print(s)

# value access  = set has no order
for i in s:
    print(i)

# change value
s.remove(10)
s.add(100)
print(s)

# discard 
se= {10,20,30}
se.discard(20)
print(se)

# clear  = to remove all element
se = {10,20,50}
a = se.clear()  # all element had clear
print(" all element remove",se)

# discard - also used to remove element

se = {10,20,50,40}
se.discard(10)  # this method want value for remove 
print( "discard set ",se)

# pop = romove random element
se = {10,20,30,40}
remov = se.pop()  # pop work on index but in case of set it remove random value because set
print(se) 
print("random element remove ",remov)
