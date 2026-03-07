marks=int(input("Give me your marks:"))
if (marks>=80 and marks<=100):
    print("grade=A+")
elif (marks>=75 and marks<80):
    print("grade=A")
elif (marks>=70 and marks<75):
    print("grade=A-")
elif (marks>=65 and marks<70):
    print("grade=B+")
elif (marks>=60 and marks<65):
    print("grade=B-")
elif (marks>=55 and marks<60):
    print("grade=C+")
elif (marks>=50 and marks<65):
    print("grade=C-")
elif (marks>=45 and marks<50):
    print("grade=D+")
elif (marks>=40 and marks<45):
    print("grade=D-")
elif (marks<40 and marks>0):
    print("grade=F")
else:
    print("Invalid value")
