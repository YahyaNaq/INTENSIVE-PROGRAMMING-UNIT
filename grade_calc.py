#Python Program to take in the marks of 5 subjects and display the grade

Eng=eval(input("Please enter marks of English: "))
PF=eval(input("Please enter marks of Programming Fundamentals: "))
ICT=eval(input("Please enter marks of ICT: "))
A_Phy=eval(input("Please enter marks of Applied Physics: "))
Calc=eval(input("Please enter marks of Calculus: "))
TMarksObt=Eng+PF+ICT+A_Phy+Calc
if TMarksObt>=400:
    print("Grade A*")
if TMarksObt>=350 and TMarksObt<400:
    print("Grade A")
if TMarksObt>=300 and TMarksObt<350:
    print("Grade B")
if TMarksObt>=250 and TMarksObt<300:
    print("Grade C")
if TMarksObt<250:
    print("Grade F")
