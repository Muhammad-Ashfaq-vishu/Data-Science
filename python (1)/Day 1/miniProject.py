
# stduent info 
name = input("Enter your name : ")
age = int(input("Enter your age : "))
student_class = input("Enter your class : ")
Roll_no = int(input("Enter your Roll_no : "))


# student marks 
english = int(input("Enter your English subject marks : "))
maths = int(input("Enter your maths subject marks : "))
CS = int(input("Enter your CS subject marks : "))
physics = int(input("Enter your physics subject marks : "))
urdu = int(input("Enter your urdu subject  marks : "))

total = english + maths + CS + physics + urdu
percentage = (total / 500) * 100


# Grade

if percentage >= 80:
    print("Your grade is A+")
elif percentage >= 70 and percentage < 80:
    print("Your grade is A")
elif percentage >= 60 and percentage < 70:
    print("Your grade is B")
elif percentage >= 50 and percentage < 60:
    print("Your grade is C")
elif percentage >= 40 and percentage < 50:
    print("Your grade is D")
else:
    print("Your grade is F")

# Check pass/fail (Pass if percentage ≥ 33).
passed = percentage >= 33 and "Pass" or "Fail"


# Check if "a" exists in student’s name.
print("Does name contain 'a'? ->", "a" in name.lower()
)
# Check if percentage is None before calculation.
if percentage is None:
    print("Percentage not calculated yet!")



# Display Report Card
print("\n---------- REPORT CARD ----------")
print("Name:", name)
print("Age:", age)
print("Class:", student_class)
print("Roll No:", Roll_no)
print("English:", english)
print("Maths:", maths)
print("CS:", CS)
print("Physics:", physics)
print("Urdu:", urdu)
print("Total:", total)
print("Percentage:", percentage)
print("Passed:", passed)





