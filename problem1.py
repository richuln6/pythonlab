def compute(s):
    n=len(s)
    x=0
    st=[]
    st1=[""]
    
    
    for i in range(n):
        if(s[i]!='=' and s[i]!=','):
            st[x]=st[x]+s[i]
        else: 
            x=x+1
    
    return st

s=compute("a=b,hello=world,d=e")
print(s,s1)
