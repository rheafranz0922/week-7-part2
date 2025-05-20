# total hour
employee_salaries = [22.15, 22.55, 23.45, 23.85, 24.32, 24.85, 25.84, 26.75]
total_hourly_rate = [round(salary * 1.3, 2) for salary in employee_salaries]

# find the underpaid salary
underpaid_salaries = [rate for rate in total_hourly_rate if 28.15 <= rate <= 30.65]

# Output
print("Underpaid Salaries (total hourly rate between $27.45 and $30.65):", underpaid_salaries)