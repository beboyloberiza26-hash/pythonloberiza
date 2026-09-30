students = {
    "Ana" : 85,
    "Ben" : 90,
    "Carlo" : 78,
    "Diana" : 95
}
print("STUDENT GRADES")
print("-----------------")
print("Ana:" , students["Ana"])
print("Ben:" , students["Ben"])
#add a new student
students["Ella"] = 88
#Update a student's grade
students["Carlo"] = 82
students["Diana"] = 91
name1 = input("Enter Student name: ")
grade1 = int(input("Enter grade:"))
students[name1] = grade1
print(students)
print("\nUpdated Student Grades")
print("-------------------------")
for name,grade in students.items():
    print(name, ":" ,grade)
search = input("\nEnter Student name to search: ")
if search in students:
    print(search, "has a grade of" , students[search])
else:
    print("Student not Found")


print()

grades = students.values()


highest = max(grades)
print("Highest grade:", highest)

minimum = min(grades)
print("Lowest grade:", minimum)

difference = highest - minimum
print("Difference:", difference)

average = sum(grades) / len(students)
print("Average:", average)
sorted_by_name = sorted(students.items())

print("\nGrades sorted alphabetically:")
for name, grade in sorted_by_name:
    print(name, ":", grade)
