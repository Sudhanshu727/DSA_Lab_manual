student_name="Sudhanshu Shekhar"
roll_number = 20
subjects = ["Mathematics", "Chemistry", "Physics", "English", "Computer Science"]
marks_obtained= [95, 93, 92, 89, 91]
total_marks = [100, 100, 100, 100, 100]
grades_secured=["A+", "A+","A+","A","A+"]

print("\n" + "=" * 100)
print(f"{'12th Grade Marksheet':^100}")
print("=" * 100)
print(f"Student Name: {student_name}")
print(f"Roll Number: {roll_number}")
print("-" * 100)
print(f"{'Subject':<30}{'Marks Obtained':<20}{'Total Marks':<20}{'Grades':<20}")
print("-" * 100)

for subs, marks, total, grade in zip(subjects, marks_obtained, total_marks,grades_secured):
    print(f"{subs:<35}{marks:<20}{total:<20}{grade:<20}")
print("="*100)
print(f"{'Total Marks':<35}{sum(marks_obtained):<20}{500:<20}{'A+':<20}")
print("="*100)

print("Percentage:", sum(marks_obtained) / 5, "%")