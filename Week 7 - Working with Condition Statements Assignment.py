# data from spreadsheets
data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# Create a set to avoid the duplicates
employees_number = set()
employees_name = set()
employees_salary = set()

# List to organize the data types
for item in data:
    if isinstance(item, bool):
        continue  # skip it
    elif isinstance(item, int) and item > 1000:
        employees_number.add(item)
    elif isinstance(item, str):
        employees_name.add(item)
    elif isinstance(item, float):
        employees_salary.add(item)

# Convert the set from the list
employees_number = sorted(list(employees_number))
employees_names = sorted(list(employees_name))
employees_salary= sorted(list(employees_salary))

# Print the results
print("Employee Numbers:", employees_number)
print("Employee Names:", employees_name)
print("Employee Salaries:", employees_salary)