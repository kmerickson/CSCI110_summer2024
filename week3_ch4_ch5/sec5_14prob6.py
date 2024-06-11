# name: sec5_14prob6.property
# purpose: takes an array of grades from 0 to 100 and assignes 
# them a grade catagory, from sec 5.14, problem 6 of
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 11, 2024

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
    49.9, 45, 44.9, 40, 39.9, 2, 0]

def assignGrade(g):
    if g < 40:
        s = "F3"
    elif 40 <= g < 45:
        s = "F2"
    elif 45 <= g <50:
        s = "F1 Supp"
    elif 50 <= g < 60:
        s = "Third"
    elif 60 <= g < 70:
        s = "Second"
    elif 70 <= g < 75:
        s = "Upper Second"
    elif g >= 74:
        s = "First"

    return s

print(xs[0])
grade = assignGrade(xs[0])

print(grade)

for i in range(len(xs)):
    print("Exam mark: "+str(xs[i]))
    grade = assignGrade(xs[i])
    print("Has a grade of: "+grade)
    print()    