  # under stand the power of list

# ordered = all element are in order way

a = [10,20,30,40,50,60]
print("element in order --->",a)

# mutable = we can update ,change , remove value 

a = [10,20,30,40,50,60]

a[0]  = 100
a[1]  = 90
a[2]  = 80
a[3]  = 70
a[4]  = 60
a[5]  = 50

print("updated list --->",a)


# Duplicate = List contain duplicate value 

a= [10,20,20,50,40,80,70,70,70,80]

print("contain duplicate --->",a)


### Creating and accessing list  == Way to acces element

fruit = ["orange","apple","banana","guava"]

print(fruit[0])  # ="orange"
print(fruit[-1]) # = "guava"
print(fruit[0:3])# = 'orange','apple','banana'

fruit[0] = "PineApple"  # list allowed to change
print(fruit[0])  
 
######  traversing on list = There are two types to traverse on list

#1. Traverse on values  = Achieve element using loop

a = [10,20,30,40,50,60]

for i in a:
    print(i)
    
print("This run on value :")


# Traverse on index  = Achieve element using index


a = [10,20,30,40,50,60]
for i in range(0,len(a)):
    print(f"{i}--> {a[i]}")
    
print("This run on index:")

print(dir(list))