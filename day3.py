# Conditional statement
x=0
if x > 0:
    print(f"{x} is positive.")
elif x<0:
    print(f"{x} is negitive.")
else:
    print(f"{x} is zero.")



    a=-10
    b=10
    if a>0 or b>0:
        print('One of them is positive.')
    else:
        print("Both are not positive.")


    # Looping in list
    fruits = ['apple', 'banana', 'mango', 'orange']
    for fruit in fruits:
        print(fruit)


    # looping in tuple
    colors = ('green', 'yello', 'red')
    for color in colors:
        print(color)


    # looping in set
    numms = [1,2,3,4,5,6,7,1,2,3]
    for num in numms:
        print(num)
    
    # looping in Dictionaries
    student_grades = {
        'bishal': 90,
        'jagriit': 56,
        'sujan': 67
    }

    for grade in student_grades:
        print(f"{grade} scored {student_grades[grade]}.")

        for student, grade in student_grades.items():
            print(student, "scored", grade)
        
        for grade in student_grades.values():
            print(grade)

        message = 'This much for today!'
        for msg in message:
            print(msg)

        for num in range(1,11):
            print(num)