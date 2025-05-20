# hourly salary
employee_salaries = [22.12, 22.65, 23.5, 23.75, 24.32, 25.25, 25.64, 28.75]

# raises funds
company_raises = []

for rate in employee_salaries:
    if 22 <= rate < 24:
        raised = round(rate * 1.05, 2)
    elif 24 <= rate < 26:
        raised = round(rate * 1.04, 2)
    elif 26 <= rate < 28:
        raised = round(rate * 1.03, 2)
    else:
        raised = round(rate * 1.02, 2)
    
    company_raises.append(raised)

# Output
print("Original Salaries:", employee_salaries)
print("Company Raises (new salary rates):", company_raises)