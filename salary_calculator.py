name = input("Enter Employee Name: ")

basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 0.20
bonus = basic_salary * 0.10

total_salary = basic_salary + hra + bonus

print("\n===== SALARY SLIP =====")

print("Employee Name :", name)
print("Basic Salary  :", basic_salary)
print("HRA           :", hra)
print("Bonus         :", bonus)
print("Total Salary  :", total_salary)
