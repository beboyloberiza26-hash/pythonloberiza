students = {}
number = int(input("Enter number of students: "))
for i in range(number):
    print("\nStudent", i + 1)
    name = input("Enter Student Name:")
    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))
print("\n===== STUDENT RECORDS =====")
highest = 0
namehighest = ""
tally = 0
for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, *grades, "Average:", round(average, 2))