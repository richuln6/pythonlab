def fractions(t1,t2):
    num=(t1[0]*t2[1])+(t1[1]*t2[0])
    den=(t1[1]*t2[1])
    res=(num,den)
    return (res)

tr=fractions((1,1),(4,2))

print(str(tr[0])+"/"+str(tr[1]))






class fractionclass:
    int num,den
    def input():
        num=input("enter the numerator")
        den=input("enter the denomenator")
        return (num,den)

fractionclass obj=new 
        
