def compute(s):
    n=len(s)
    x=0
    st=[]
    str1,str2="",""
    for i in range(n):
        if(s[i]!='=' and s[i]!=','):
            str2=str2+s[i]
            
        elif s[i]=='=':
            str1=str2
            str2=""
        else : 
            st.append((str1,str2))
            str1=str2=""    
    st.append((str1,str2))        
    return st

S=compute("a=b,hello=world,d=e")
print(S)






