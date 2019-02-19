


def fib(n):
    x,y=0,1
    for i in range(n):
        print (x)
        x,y=y,x+y
        

fib(10)



def fib():
    x,y=0,1
    print(x)
    print(y)
    while(True):
        yield (x+y)
        x,y=y,x+y


x=fib()
for i,j in zip(x,range (10)):
    print(i)

        

