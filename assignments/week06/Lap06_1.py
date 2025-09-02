# """ เขียน function ชื่อ welcome_message ที่มีคุณสมบัติดังนี้:

# รับ parameter 2 ตัว คือ name และ course
# return ข้อความต้อนรับในรูปแบบ string
# รูปแบบ: "Welcome [name] to [course] class!"
name = "zaza007"
course = "830"

def welcome_message(name, course):
    print(f"Welcome {name} to {course} class!")

welcome_message(name, course)

# """ เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

# รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
# return string ที่จัดรูปแบบข้อมูลผู้ใช้
# รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

# """

def create_user_profile(username, age=18, premium=False):
    user_type = "Premium User" if premium else "Standard User"
    return f"{username} (age: {age}) - {user_type}"


username = input("enter name: ")
age_input = input("enter your age (leave blank for default 18): ")
premium_input = input("Are you a premium user? yes/no, default no: ")

age = int(age_input) if age_input else 18
premium = premium_input.strip().lower() == "yes"

print(create_user_profile(username, age, premium))


# """ เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

# รับ list ของคะแนน (ตัวเลข)
# return dictionary ที่มี:

# total: ผลรวมของคะแนนทั้งหมด
# average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
# highest: คะแนนสูงสุด
# lowest: คะแนนต่ำสุด
# passed: จำนวนคะแนนที่ >= 70 """


def analyze_scores(score_box):
    total = sum(score_box)
    average = round(total / len(score_box), 1) if score_box else 0
    highest = max(score_box) if score_box else None
    lowest = min(score_box) if score_box else None
    passed = len([s for s in score_box if s >= 70])
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }
score_box = []
print("welcome my program analyze_score")
for x in range(1, 4):
    score = int(input(f"enter score round{x}: "))
    score_box.append(score)

for index, score in enumerate(score_box, 1):
    if score >= 80:
        print(f"round {index}: very good")
    elif score >= 70:
        print(f"round {index}: pass")
    else:
        print(f"round {index}: not pass")

result = analyze_scores(score_box)
print("information score: {}".format(result))


# รับ parameter text เป็น string
# นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
# return dictionary ที่มี vowels และ consonants counts
# ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """


def count_vowels_consonants(text):
    vowels_set = set("aeiou")
    vowels = 0
    consonants = 0
    for char in text.lower():
        if char.isalpha():
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1
    return {"vowels": vowels, "consonants": consonants}

text = input("enter another word:")
count_pass = count_vowels_consonants(text)
print(count_pass)



""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:

รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """

def calculate_circle(radius):
    pi = 3.14159
    area = round(pi * radius * radius, 2)
    circumference = round(2 * pi * radius, 2)
    return {"area": area, "circumference": circumference}

radius_input = float(input("Enter circle radius: "))
circle_info = calculate_circle(radius_input)
print("Circle info:", circle_info)

        









