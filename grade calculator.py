print("📊 Grade Statistics Calculator 📊\n")

grades = []
num_students = int(input("How many students? "))
for i in range(num_students):
    grade = int(input(f"Enter grade for student {i+1}: "))
    grades.append(grade)
total = 0
for grade in grades:
    total += grade
average = total / num_students
passing = 0
failing = 0

for grade in grades:
    if grade >= 60:
        passing += 1
    else:
        failing += 1
print(f"\n📈 Results:")
print(f"Average: {average:.1f}")
print(f"Passing (60+): {passing}")
print(f"Failing: {failing}")
if average >= 70:
    print("🎉 Great class performance!")
elif average >= 60:
    print("👍 Good class performance")
else:
    print("📚 Class needs more support")
