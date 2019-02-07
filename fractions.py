def fractions(t1,t2):
    num=(t1[0]*t2[1])+(t1[1]*t2[0])
    den=(t1[1]*t2[1])
    res=(num,den)
    return (res)

tr=fractions((1,1),(4,2))

print(str(tr[0])+"/"+str(tr[1]))





class fractionclass:
    def __init__(self,a,b):
        self.numerator=a
        self.denomenator=b
    def add(f1,f2):
        num=(f1.numerator*f2.denomenator)+(f1.denomenator*f2.numerator)
        den=f1.denomenator*f2.denomenator
        return (num,den)
f1=fractionclass(2,4)
f2=fractionclass(1,2)
t=fractionclass.add(f1,f2)
print(str(t[0])+"/"+str(t[1]))


def fractiondictionary(t1,t2):
    d={}
    d["Numerator"]=(t1[0]*t2[1])+(t2[0]*t1[1])
    d["denomenator"]=t1[1]*t2[1]
    return d

D=fractiondictionary((2,4),(1,2))
print(str(D["Numerator"])+"/"+str(D["denomenator"]))

def fractionslist(t1,t2):
    num=(t1[0]*t2[1])+(t1[1]*t2[0])
    den=(t1[1]*t2[1])
    res=[num,den]
    return res

d=fractionslist((1,1),(4,2))
print(str(d[0])+"/"+str(d[1]))


def frac(n1,d1,n2,d2):
    n=(n1*d2)+(n2*d1)
    d=d1*d2
    return(n,d)

tr=frac(1,2,2,4)
print(str(tr[0])+"/"+str(tr[1]))


