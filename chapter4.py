#1
import random
x=random.randint(5,10)
print(x)


#2
def print_lyrics():
    print("So baby pull me closer")
    print("on the backseat of you're rover")
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()


#6

def computepay(hours,rate):
    try:
        if hours<=40:
            pay=hours*(rate)
        else:
            pay=(40*(rate))+((hours-40)*1.5*rate)
        return pay
    except:
        return("Enter Numeric Input")

hours=float(input("Enter Hours"))
rate=float(input("enter rate"))
s=computepay(hours,rate)
print(s)


#7
def grade_score(grade):
    try:
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
    except:
        return "Bad Score"

grade=input("Enter Score:")
try:
    g=grade_score(float(grade))
except:
    g="Bad Score"
print(g)
