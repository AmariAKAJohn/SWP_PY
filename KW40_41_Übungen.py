#Normal Division vs Floor Division

#Normal Division
print(5/2)
# Here the output will be 2.5 because it is normal division and it will return the float value.

#Floor Division
print(5//2)
# Here the output will be 2 because it is floor division and it will always round down to the nearest integer value.
#----------------------------------------------------------
# Logical Operators
# and, or, lt, eq

print(5>3 and 5<10)
# Here the output will be True because both conditions are true.

print(5>3 or 5>10)
# Here the output will be True because one or both of the conditions are true.

print(5<3) #lt
# Here the output will be False because 5 is not less than 3.

print(5==5) #eq
# Here the output will be True because 5 is equal to 5.

#----------------------------------------------------------
# Order of Operations
# multiplications/divisions > additions/subtractions
# can use () to change order

print(5+3*2)
# First 3*2 and then + 5 = 11

print((5+3)*2)
# First 5+3 and then * 2 = 16
#----------------------------------------------------------

# Difference between == and is

a = [1,2,3]
b = [1,2,3]
print(a == b)
# Here the output will be True because the values of a and b are equal.

print(a is b)
# Here the output will be False because a and b are two different objects.
# That means with == we can check the values and with is we can check the objects.

#----------------------------------------------------------
# Free Instances with "del"

a = 5
print(a)
del a
#print(a)
# Here before the del a the output will be 5 and after the del a the output will be an error because a is "deleted".

#----------------------------------------------------------

#Tuple, Range, Set

#Tuple: A tuple is a collection which is unchangeable. 
a = (1,2,3)
print(a)

#Range: A range is a collection which is unchangeable. 
a = range(10)
print(a)
for i in a:
    print(i)

# Set: A set is a collection which is unordered and unindexed. Set can not have two items with the same value. 
a = {1,2,3}
print(a)

