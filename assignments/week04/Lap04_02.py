def even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def odd_numbers(numbers):
    return [n for n in numbers if n % 2 != 0]

def average(numbers):
    return sum(numbers) / len(numbers)

def greater_than_average(numbers):
    avg = average(numbers)
    return [n for n in numbers if n > avg]

def show_statistics(numbers):
    print(f"sum {sum(numbers)}")
    print(f"average {average(numbers):.2f}")
    print(f"min {min(numbers)}")
    print(f"max {max(numbers)}")


number_box = []
print("enter number 10 time. ")
for x in range(1, 11):
    num = int(input(f"round {x}. "))
    number_box.append(num)

print(f"original list {number_box}")

even_number = even_numbers(number_box)
odd_number = odd_numbers(number_box)
greater_than_avg = greater_than_average(number_box)

print(f"Even number {even_numbers}")
print(f"Odd number {odd_numbers}")
print(f"Number than average {greater_than_avg}")

print("Statistic")
show_statistics(number_box)
