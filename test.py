def add(a,b):
    return a+b

x=add(1,2)
print(x)

def compare(a,b):
    if a<b :
        return a
    else : 
        return b 

y=compare(20,10)
print(y)

def compare3(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c

z=compare3(50,100,30)
print(z)

