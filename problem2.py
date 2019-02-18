def split_string(s):
    t=s.split(";")
    d={}
    for i in t:
        s=i.split("=")
        d.update({s[0]:s[1]})
    return d
d=split_string("a=b;c=d;e=f;g=h")
print(d)
