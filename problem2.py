def list_to_string(l):
    s1=""
    s4=""
    for i in l:
        s3="=".join(i[0]+i[1])
        s4=s4+s3+";" 
    return s4[:-1:]
l=list_to_string([('a','b'),('c','d'),('e','f'),('g','h')])
print(l)
        


def split_string(s):
    t=s.split(";")
    d={}
    for i in t:
        s=i.split("=")
        d.update({s[0]:s[1]})
    return d
d=split_string("a=b;c=d;e=f;g=h")
print(d)
