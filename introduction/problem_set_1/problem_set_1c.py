from introduction.problem_set_1b import calc_savings_raise

def calc_savings_rate(annual_salary, total_cost, portion_down_pmt, roi, current_savings, semi_annual_raise, num_months, tolerance):
    portion_saved = .5
    bisection_steps = 0
    output = calc_savings_raise(annual_salary=annual_salary, 
                        total_cost=total_cost,
                        portion_down_pmt=portion_down_pmt,
                        roi=roi,
                        current_savings=current_savings,
                        semi_annual_raise=semi_annual_raise,
                        portion_saved = portion_saved,
                        tolerance=tolerance)
    while output != num_months:
        bisection_steps += 1
        if output > num_months:
            portion_saved = portion_saved + (portion_saved / 2)
        else:
            portion_saved = portion_saved - (portion_saved / 2)
        output = calc_savings_raise(annual_salary=annual_salary, 
                        total_cost=total_cost,
                        portion_down_pmt=portion_down_pmt,
                        roi=roi,
                        current_savings=current_savings,
                        semi_annual_raise=semi_annual_raise,
                        portion_saved = portion_saved,
                        tolerance=tolerance)
        if portion_saved > 1:
            print(f"Not Possible to pay down payment in {num_months} months.")
            return -1
    print(f"Search completed in {bisection_steps} steps.")
    return portion_saved


if __name__ == '__main__': 
    PORTION_DOWN_PMT = .25
    ROI = .04
    CURRENT_SAVINGS = 0
    SEMI_ANNUAL_RAISE = .07
    TOTAL_COST = 1_000_000
    NUM_MONTHS = 36
    TOLERANCE = 100
    annual_salary = int(input("Please enter Annual Salary: $"))
    best_rate = calc_savings_rate(annual_salary=annual_salary,
                                    total_cost=TOTAL_COST,
                                    portion_down_pmt = PORTION_DOWN_PMT,
                                    roi=ROI,
                                    current_savings=CURRENT_SAVINGS,
                                    semi_annual_raise=SEMI_ANNUAL_RAISE,
                                    num_months=NUM_MONTHS,
                                    tolerance=TOLERANCE
                                    )
    if best_rate == -1:
        pass
    else:
        print(f"The rate of {round(best_rate, 4)} will allow for a down payment of ${TOTAL_COST * PORTION_DOWN_PMT} in {NUM_MONTHS} months")