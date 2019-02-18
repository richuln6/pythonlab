#ex-1 , 2
def calc_pay():
    try:
        hours=float(input("Enter Hours"))
        rate=float(input("enter rate"))
        if hours<=40:
            pay=hours*(rate)
        else:
            pay=(40*(rate))+((hours-40)*1.5*rate)
        return pay
    except:
        return("Enter Numeric Input")
s=calc_pay()
print(s)


#ex-3
def grade_score(grade):
    if grade>0.0 and grade<1.0:
        if grade>=0.9:
            return("A")
        elif grade>=0.8:
            return "B"
        elif grade>=0.7:
            return "C"
        elif grade>=0.6:
            return "D"
        else :
            return "F"
    else:
        return "Score Out Of Range"

g=grade_score(0.5)
print(g)
    
