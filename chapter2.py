#ex-2
def print_hello():
    name=input("Enter Your Name")
    return("hello "+name)

s=print_hello()
print(s)


#ex-3
def calc_pay():
    hours=float(input("Enter Hours"))
    rate=float(input("enter rate"))
    pay=hours*(rate)
    return pay
s=calc_pay()
print(s)


#ex-5
def celsius_to_fahrenheit():
    c=float(input("enter temp in celsius"))
    f=float((c*1.8)+32)
    return f

s=celsius_to_fahrenheit()
print(str(s)+" in Fahrenheit")


