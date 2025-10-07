# """
# Create a grade processing system with the following requirements:

# A global variable passing_grade = 50

# (1) A function input_students(num_students) that:

# - Creates and returns a list of dictionaries
# - Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

# (2) A function calculate_averages(students) that:

# - Uses nested loops to calculate each student's average
# - Adds an 'average' key to each student dictionary
# - Modifies the original list (demonstrate list mutability)

# (3) A function display_results(students) that:

# - Loops through students
# - Uses the global passing_grade to determine pass/fail
# - Prints each student's name, average, and status (PASS/FAIL)
# """


passing_grade = 50

def input_students(num_students):
	students = []
	for i in range(num_students):
		name = input(f"Enter name for student {i+1}: ")
		scores = []
		for j in range(3):
			score = float(input(f"Enter score {j+1} for {name}: "))
			scores.append(score)
		students.append({'name': name, 'scores': scores})
	return students

def calculate_averages(students):
	for student in students:
		total = 0
		for score in student['scores']:
			total += score
		average = total / len(student['scores'])
		student['average'] = average

def display_results(students):
	for student in students:
		status = "PASS" if student['average'] >= passing_grade else "FAIL"
		print(f"{student['name']}: Average = {student['average']:.2f} - {status}")

if __name__ == "__main__":
	num_students = int(input("How many students? "))
	students = input_students(num_students)
	calculate_averages(students)
	display_results(students)


# """
# Write a program that analyzes daily temperatures for a week:

# Create a function get_temperatures() that:

# - Uses a local list to store 7 temperature values (use input or predefined values)
# - Returns the list

# Create a function analyze_temps(temp_list) that:

# - Calculates and returns the average temperature (local variable)
# - Finds and returns the highest temperature
# - Finds and returns the lowest temperature
# - Returns all three values as a tuple

# Create a function display_analysis(avg, high, low) that prints the results nicely formatted

# Example Output:
# Temperature Analysis for the Week:
# Average: 23.5 C
# Highest: 28 C
# Lowest: 19 C

# """

def get_temperatures():
	temps = []
	for i in range(7):
		temp = float(input(f"Enter temperature for day {i+1}: "))
		temps.append(temp)
	return temps

def analyze_temps(temp_list):
	avg = sum(temp_list) / len(temp_list)
	high = max(temp_list)
	low = min(temp_list)
	return (avg, high, low)

def display_analysis(avg, high, low):
	print("Temperature Analysis for the Week:")
	print(f"Average: {avg:.2f} C")
	print(f"Highest: {high} C")
	print(f"Lowest: {low} C")

if __name__ == "__main__":
	num_students = int(input("How many students? "))
	students = input_students(num_students)
	calculate_averages(students)
	display_results(students)


	temps = get_temperatures()
	avg, high, low = analyze_temps(temps)
	display_analysis(avg, high, low)