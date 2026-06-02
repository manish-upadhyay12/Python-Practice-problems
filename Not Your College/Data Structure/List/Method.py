  # All method of list
 # Note = we can store everything in list either function like print;
  # Homogenous  = same data type
#  non - homogenous  = different data type

# 1. append = this method not return anything only modify the list
a = [10,20,30,40]
a.append(10000)   
print(a)

# 2. remove = remove element from list   ,WE pass value instead of index
 
a = [10,20,30,40]
a.remove(20)
print(a)

#3.  pop = also use to remove value ,we pass index 

a= [0,20,30,40,50]
p = a.pop(0)
print(a)
p = a.pop(1)
print(a)
p = a.pop(2)
print(a)
#p = a.pop(3) this index does not exist because list modidy line by line

#4.  clear = use to clear all element in list
a= [10,20,30,40]
a.clear()  # clear never return anything
print(p)

#5.  sort = use to sort all element in list 

a= [20,80,40,5,10,30,40,20]
a.sort()  # not return anything
print(a)

a.sort(reverse = True)
print(a)

# 6. insert = use to insert element at any index(remove index,value add)

a = [70,50,20,30,40]
a.insert(0,100)
print(a)
  

