grades = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Ayesha": 95,
    "Usman": 88
}

total = 0
for score in grades.values():
    total += score

print("Class average:", total / len(grades))

top_name = ""
top_score = 0

for name, score in grades.items():
    if score > top_score:
        top_name = name
        top_score = score

print("Highest scorer:", top_name, "-", top_score)

name = input("Enter student name: ")
print("Score:", grades.get(name, "Not found"))