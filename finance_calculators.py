import math

# Investment calculator to determine interest earnt or amount paid on a home loan

print('''Choose either 'Investment' or 'bond' from the menu below to proceed:

Investment -- to calculate the amount of interest you'll earn in interest

Bond  -- to calculate the amount you'll have to pay on a home loan''')

# Input from user for either investment or bond

invest_or_bond = input(str("Please enter Investment or Bond\n")).lower()

if invest_or_bond == "investment":
        p = float(input("How much are you depositing?\n£"))
        r = float(input("At which interest rate percent?\n%"))
        r = (r/100) / 12
        t = float(input("How many years are you planning to invest for? \n"))
        simple_int = str(
            input("Choose 'Simple' or 'Compound' interest. \n")).lower()

        if simple_int == "simple":
            "simple" == simple_int
            simple_int = p*(1 + r * t)
            total = simple_int
            print(f"Your interest earned over {t} years will be £{total:.2f}".format())

        elif simple_int == "compound":
            simple_int = p*math.pow((1+r), t)
            total = simple_int
            print(f"Your interest earned over {t} years will be £{total:.2f}".format())

#Bond option
elif invest_or_bond == "bond":
        p = float(input("What is the current value of the house?\n£"))
        i = float(input("At which interest rate percent?\n%"))
        i = ((i/100)/12)
        n = float(input("How many months you plan to repay? \n"))
        monthly = float(math.floor((i*p)/(1 - (1+i)**(-n))))
        print(f"Your monthly repayment will be {monthly:.2f}".format())

else:
    print("Please enter a valid input. Try again.")
