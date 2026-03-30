raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for s in raw_students:
    # clean name
    name = s["name"].strip().title()
    
    # convert roll
    roll = int(s["roll"])
    
    # convert marks
    marks = []
    for m in s["marks_str"].split(", "):
        marks.append(int(m))
    
    # check valid name
    valid = True
    for word in name.split():
        if not word.isalpha():
            valid = False
    
    if valid:
        print("✓ Valid name")
    else:
        print("✗ Invalid name")
    
    # print profile
    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("================================")
    
    cleaned_students.append({"name": name, "roll": roll, "marks": marks})


# print for roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print("\nSpecial Output:")
        print(s["name"].upper())
        print(s["name"].lower())