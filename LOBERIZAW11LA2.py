print("==== STUDENT PROGRAM INFORMATION FILTER ====")
print(" by LOBERIZA, CHEIJAY PAUL B.")
print()
loberiza_students = [("Jonah Perez", "BSCS", 1),
                     ("Alex Santos", "BSMT", 2),
                     ("Micah Mendoza", "BSCS",2),
                     ("Allen Torres", "BSMT",1),
                     ("Kristana Sarabia", "BSCS",3),
                     ("Josiah Quistadio", "BSMT", 4),
                     ("Jhea Canono", "BSCS", 4),
                     ("Dean Bustamante", "BSMT", 3)]
print("Student Information")
for student in loberiza_students:
    print("Name:", student[0])
    print("Program:", student[1])
    print("Year:", student[2])
    print()

search = input("Enter program to search: ")
print(f" STUDENTS IN {search.upper()} ")
found = 0

for student in loberiza_students:
    if student[1].lower() == search.lower():
        print("\nName:", student[0])
        print("Program:", student[1])
        print("Year:", student[2])
        found = found + 1

if found == 0:
    print("\nNo student found in that program.")
else:
    print("\nSearch complete.")