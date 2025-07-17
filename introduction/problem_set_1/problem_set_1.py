


def calc_months_savings(annual_salary, portion_saved, total_cost, portion_down_pmt, roi, current_savings):
    num_months = 0
    while current_savings <= (total_cost * portion_down_pmt):
        current_savings += (annual_salary * portion_saved / 12) + (current_savings * roi / 12)
        num_months += 1
    return num_months


if __name__ == '__main__':
    PORTION_DOWN_PMT = .25
    ROI = .04
    CURRENT_SAVINGS = 0
    annual_salary = int(input("Please enter Annual Salary: $"))
    portion_saved = float(input("Please enter portion of salary to save: "))
    total_cost = int(input("Please enter total cost of home: "))
    num_months = calc_months_savings(annual_salary=annual_salary,
                                    portion_saved=portion_saved, 
                                    total_cost=total_cost,
                                    portion_down_pmt = PORTION_DOWN_PMT,
                                    roi=ROI,
                                    current_savings=CURRENT_SAVINGS
                                    )
    print(f"You will need {num_months} months to purchase your dream home.")