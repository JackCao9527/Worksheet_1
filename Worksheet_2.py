name = input("Please enter your name: ")
print ("Good day,", name)

number = (9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5)
print ("The answer is: ", number)

x = float(input("Please enter the value of x: "))
y = (3 * x ** 2 + 5 * x - 2)
print ("The valur of y is: ", y)

Kilometres =  14
Miles = 14 / 1.6
Minutes = 45.30
Hours = 45.30 / 60
Average_speed = (Miles / Hours)
print ("The average speed is ", Average_speed)

population = 312032486
seconds = 5 * 365 * 24 * 60 * 60
birth = seconds // 7
death = seconds // 13
immigrant = seconds // 45
New_population = population + birth - death + immigrant
print ("The new population is: ", New_population)

Student_mark = float(input("Please enter mark of the student: "))
if Student_mark >= 80:
    grade = 'A'
elif Student_mark >=70:
    grade = 'B'
elif Student_mark >= 60:
    grade = 'C'
elif Student_mark >= 50:
    grade = 'D'
else:
    grade = ('F')
print ("The student has gotten", grade + "-greade")

x = float(input("Please enter the value of x: "))
y = float(input("please enter the value of y: "))
if x > 0 and y > 0:
    print ("The point is in quadrant 1")
elif x < 0 and y > 0:
    print ("The point is in quadrant 2")
elif x < 0 and y < 0:
    print ("The point is in quadrant 3")
elif x > 0 and y < 0:
    print ("The point is in quadrant 4")
else:
    print ("origin")

number = int(input("Please enter a number: "))
if number % 2 == 0:
    print ("even")
else:
    print ("odd")

angle1 = int(input("Please enter the degree for angle1: "))
angle2 = int(input("please enter the degree for angle2: "))
angle3 = int(input("Please enter the defree for angle3: "))
if angle1 + angle2 + angle3 == 180:
    if angle1 == angle2 == angle3:
        print ("equilateral")
    elif angle1 == angle2 or angle2 == angle3 or angle3 == angle1:
        print ("isoceles")
    else:
        print ("scalene")
else:
    print ("error")