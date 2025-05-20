# Salary
employee_salary = [22.42, 22.65, 23.35, 23.65, 24.32, 25.55, 25.84, 28.65]


total_hourly_rate = [round(salary * 1.3, 2) for salary in employee_salary]

# Step 2: Find the value
max_total_rate = max(total_hourly_rate)

# Step 3: Display results
print("Total Hourly Rates (with 30% benefits):", total_hourly_rate)
print("Maximum Total Hourly Rate:", max_total_rate)

# Step 4: Check budget
if max_total_rate > 37.30:
    print("⚠️ WARNING: Someone's salary may be a budget concern.")