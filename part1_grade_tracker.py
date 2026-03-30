# ---------------- TASK 1 ----------------
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

print("\n=== TASK 1 ===")
for s in raw_students:
    name = s["name"].strip().title()
    roll = int(s["roll"])
    marks = list(map(int, s["marks_str"].split(", ")))

    valid = all(word.isalpha() for word in name.split())

    print(f"{name}:", "✓ Valid name" if valid else "✗ Invalid name")

    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")

    cleaned_students.append({"name": name, "roll": roll, "marks": marks})

for s in cleaned_students:
    if s["roll"] == 103:
        print("\nSpecial Output:")
        print(s["name"].upper())
        print(s["name"].lower())


# ---------------- TASK 2 ----------------
print("\n=== TASK 2 ===")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

for i in range(len(subjects)):
    m = marks[i]

    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"{subjects[i]} : {m} -> {grade}")

total = sum(marks)
avg = round(total / len(marks), 2)

print("Total:", total)
print("Average:", avg)

print("Highest:", subjects[marks.index(max(marks))], max(marks))
print("Lowest :", subjects[marks.index(min(marks))], min(marks))


# ---------------- TASK 3 ----------------
print("\n=== TASK 3 ===")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

pass_c = fail_c = 0
top_name = ""
top_avg = 0
sum_avg = 0

print("Name              | Average | Status")
print("--------------------------------------")

for name, marks in class_data:
    avg = round(sum(marks)/len(marks), 2)
    sum_avg += avg

    if avg >= 60:
        status = "Pass"
        pass_c += 1
    else:
        status = "Fail"
        fail_c += 1

    if avg > top_avg:
        top_avg = avg
        top_name = name

    print(f"{name:<18} | {avg:^7} | {status}")

print("\nPassed:", pass_c)
print("Failed:", fail_c)
print("Topper:", top_name, top_avg)
print("Class Avg:", round(sum_avg/len(class_data), 2))


# ---------------- TASK 4 ----------------
print("\n=== TASK 4 ===")

essay = "   python is great. python is easy to learn. many love python   "

clean_essay = essay.strip().lower()
print("Clean:", clean_essay)

print("\nTitle Case:", clean_essay.title())

print("\nCount:", clean_essay.count("python"))

print("\nReplace:", clean_essay.replace("python", "Python 🐍"))

sentences = clean_essay.split(". ")
print("\nSentences:", sentences)

print("\nNumbered:")
for i, s in enumerate(sentences, 1):
    if not s.endswith("."):
        s += "."
    print(f"{i}. {s}")