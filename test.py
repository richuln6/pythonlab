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

z=compare3(30,100,30)
print(z)

b=5<7<8
print(b)

a=1
b=2
c=3
print(a if a<b and a<c else b if b<a and b<c else c) 

def comparetuples(a,b):
    if((a,a)<(b,c)):
            return a
    else:
        return b

d=comparetuples(100,200)
print(d)
