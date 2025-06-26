#!/usr/bin/env python3

# define the annual rate ranges for each product
RATE_RANGES = {
    'WL': [4, 5, 6, 7],
    'IUL': [8, 9, 10, 11, 12]
}

YEARS = [5, 10, 15, 20, 25]

def future_value(monthly, annual_rate, years):
    """
    Future value of a series of monthly payments at an annual_rate,
    compounded monthly.
    """
    r = annual_rate / 100
    n = years * 12
    return monthly * ((1 + r/12)**n - 1) / (r/12)

def prompt_plan():
    while True:
        plan = input("Choose policy type (WL or IUL): ").strip().upper()
        if plan in RATE_RANGES:
            return plan
        print("Invalid choice. Enter 'WL' or 'IUL'.")

def prompt_monthly():
    while True:
        val = input("Enter monthly contribution amount (e.g. 55): ").strip()
        try:
            m = float(val)
            if m > 0:
                return m
            print("Please enter a positive number.")
        except ValueError:
            print("Not a valid number. Try again.")

def main():
    print("\n=== Cash Growth Projection ===\n")
    plan = prompt_plan()
    monthly = prompt_monthly()

    print(f"\nPolicy: {plan}   Monthly contribution: ${monthly:.2f}\n")
    header = "Rate".ljust(8) + "".join(f"{yr:>12}" for yr in YEARS)
    print(header)
    print("-" * len(header))

    for rate in RATE_RANGES[plan]:
        row = f"{str(rate) + '%':<8}"
        for yr in YEARS:
            fv = future_value(monthly, rate, yr)
            row += f"{fv:12.2f}"
        print(row)

if __name__ == "__main__":
    main()
