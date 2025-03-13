##def switchargskwargs(**kwargs, *args):
 ##   print(kwargs)
 ##   print(args)

##switchargskwargs(1, 2, 3, a=4, b=5, c=6)

#Args ist keine Liste und kein Dictionary, sondern ein Tuple

# BEISPIEL
def sum_recursive(*args):
    if not args: 
        return 0
    return args[0] + sum_recursive(*args[1:])


#Inner Functions
def inneradd(firstnumber):
    def addwith(secondnumber):
        return firstnumber + secondnumber
    return addwith

add5 = inneradd(5)
print(add5(3))
# or
print(inneradd(5)(3))

#Args:

def add(*args):
    return sum(args) # Benützt sum() weil args ein Tuple ist

print(add(1, 2, 3, 4, 5)) 

#Kwargs:

def add(**kwargs):
    return sum(kwargs.values()) #Benützt jetzt values() statt sum() weils ein Dictionary ist

#Beide Zusammen:

def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(add(1, 2, 3, 4, 5, a=6, b=7, c=8, d=9, e=10)) # Bei Kwargs müssen keys und values angegeben werden


print(add(*(1,2,3,4,5)))