a = int(input("What would you like your first number to be?"))
b = int(input("What would you like your second number to be?"))

c = a + b


"""
Addition
Subtraction
Multiplication
Division
Ratio - Returns either as a decimal or percentage based on parameter. Also should use Addition function as part of ratio function
"""


#addition
def add(a,b):
    return a+b

##subtraction
def sub(a,b):
    return a-b

#multiplication
def mul(a,b):
    return a*b
#division
def div(a,b):
    return a/b

#ratio

def ratio(a,b, is_percentage=True):
    if is_percentage==True:
        r1=(a/(a+b))*100
    else:
        r1=(a/(a+b))
    return r1

print(f"addition result:{add(a,b)}")
print(f"subtraction result:{sub(a,b)}")
print(f"multiplication result:{mul(a,b)}")
print(f"division result:{div(a,b)}")
print(f"ratio result:{ratio(a,b)}")





