num_grades = int(input("Enter the number of grades: "))

A = 0
B = 0
C = 0
D = 0
F = 0

for _ in range(num_grades):
    grade = int(input("Enter a grade: "))
    if 90 <= grade <= 100:
        A += 1
    elif 75 <= grade <= 89:
        B += 1
    elif 60 <= grade <= 74:
        C += 1
    elif 50 <= grade <= 59:
        D += 1
    elif 0 <= grade <= 49:
        F += 1

total_grades = num_grades
percentage_A = (A / total_grades) * 100
percentage_B = (B / total_grades) * 100
percentage_C = (C / total_grades) * 100
percentage_D = (D / total_grades) * 100
percentage_F = (F / total_grades) * 100

if A == 1:
    print(f"A: {A} grade ({percentage_A:.2f}%)")
else:
    print(f"A: {A} grades ({percentage_A:.2f}%)")

if B == 1:
    print(f"B: {B} grade ({percentage_B:.2f}%)")
else:
    print(f"B: {B} grades ({percentage_B:.2f}%)")

if C == 1:
    print(f"C: {C} grade ({percentage_C:.2f}%)")
else:
    print(f"C: {C} grades ({percentage_C:.2f}%)")

if D == 1:
    print(f"D: {D} grade ({percentage_D:.2f}%)")
else:
    print(f"D: {D} grades ({percentage_D:.2f}%)")

if F == 1:
    print(f"F: {F} grade ({percentage_F:.2f}%)")
else:
    print(f"F: {F} grades ({percentage_F:.2f}%)")