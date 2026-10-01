LoberizaSalary = {"E104": {
    "EmpName" : "Kristana Sarabia",
    "Dailyltrs": [8,9,8.5,10,8]

},
    "E601": {
        "EmpName" : "Rene Discarte",
        "Dailyltrs" : [9,10,8,8,9]

    }
}

weeklybasic = 9000
rate_per_hour = weeklybasic / 40

print("---- Registered Emploee IDs ----")
for loberiza_emp_id in LoberizaSalary:
        print(f"- {loberiza_emp_id}")
loberiza_search_id = input("Enter Employee ID to search: ").strip()
if loberiza_search_id in LoberizaSalary:
    loberiza_employee = LoberizaSalary[loberiza_search_id]
    loberiza_name = loberiza_employee["EmpName"]
    loberiza_hours_list = loberiza_employee["Dailyltrs"]
    loberiza_total_weeklyhours = sum(loberiza_hours_list)
    loberiza_overtime_pay = 0.0
    for hours in loberiza_hours_list:
        if hours > 8:
            loberiza_excess_hours = hours - 8
            loberiza_overtime_pay =  loberiza_overtime_pay + (loberiza_excess_hours * (rate_per_hour * 1.5))
    loberiza_gross_pay = (40 * rate_per_hour) + loberiza_overtime_pay

    print("\n [RECORD FOUND]")
    print(f"Employee Name      : {loberiza_name}")
    print(f"Total Weekly Hours : {loberiza_total_weeklyhours:.2f} hours")
    print(f"Excess Hours       : {loberiza_excess_hours:.2f} hours")
    print(f"Rate Per Hour      : PHP {rate_per_hour:.2f}")
    print(f"Total Overtime Pay : PHP {loberiza_overtime_pay:.2f}")
    print(f"Gross Pay          : PHP {loberiza_gross_pay:.2f}")

else:
    print(f"\nEmployee ID '{loberiza_search_id}' not found.")