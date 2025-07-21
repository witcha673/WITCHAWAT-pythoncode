#WITCHAWAT SUPAVANANIMIT 6730202416 SEC:830
#PROGRAM finace_count.py
    

salary = float(input("Enter your salary: "))
house_cost = float(input("Enter the cost of the house: "))
food_cost = int(input("Enter the monthly food cost: "))
tranport_cost = int(input("Enter the monthly transport cost: "))
another_cost = int(input("Enter any other monthly cost: "))
print("keep for emergency fund 15.0 and investment 10.5\n")

total_fixed_cost = house_cost + tranport_cost
total_Variable_cost = food_cost + another_cost
total_all_cost = total_fixed_cost + total_Variable_cost

emergency_fund = salary * (10.5 / 100)#keep 10.5% for emergency fund
invesment = salary * (15.0 / 100) #keep 15.0% for investment
remaining_salary = salary - total_all_cost #remaining salary after all costs
anvalable_money_for_saving = remaining_salary- emergency_fund - invesment #available money for saving after emergency fund and investment
expense_ratio = (total_all_cost / salary) * 100

print("===MONTHLY BUDGET REPORT===")
print(f"salary: {salary}")
print(f"fixed cost: {total_fixed_cost}")
print(f"variable cost: {total_Variable_cost}")
print(f"total cost: {total_all_cost}")
print(f"remaining salary: {remaining_salary}\n")

print("===SAVINGBREAKDOWN===")
print(f"emergency fund: {emergency_fund}")
print(f"investment: {invesment}")
print(f"anvalable money for save: {anvalable_money_for_saving}\n")

print("===ANALYSIS===")
print(f"expense ratio: {expense_ratio:.2f}%\n") 