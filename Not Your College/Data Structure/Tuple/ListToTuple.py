#   Under stand tuple how to change list into tuple  , how to access tuple element
#  "Question" : change ,list to tuple and check data type
#  "Question" : how to access element in tuple
#   Question : check when we change value in tuple is it change or not and whay error come
#   Question  : packing and unpacking of tuple


# check value change or not
l = [1, 2, 3, 4, 5, 6, 7]
tup = tuple(l)
print(type(tup))
print(type(l))

# how to access element in tuple
# note  = we can not change element  of tuple but reassign the tuple

tup = (3, 1, 4, 11)
print(tup[0])
print(tup[1])

# check value change or not in tuple
tup = (1, 2, 3, 4, 5, 6, 7)

tup[0] = 10  # conclusion : we can not change element directly
# TypeError: 'tuple' object does not support item assignment
print(tup)


# packing and unpacking of tuple

def student():
    return "Manish upadhyay", 1250500919, "raya(mathura)", "GLA university"


detail = student()
print(detail)  # it will be print in packing form

# unpacking tuple element

# note :interpreter dont know which one is name and rollNumber if we want to access write fix position correctely
name,  rollNumber, address,  college = detail  # unpacking element
print(name, rollNumber, address, college)     # print unpack element
