class Roi(): 
    def __init__(self, ):
        self.total_monthly_income = 0
        self.total_monthly_expenses = 0
        self.total_monthly_cash_flow = 0
        self.total_annual_cash_flow = 0
        self.total_investment = 0
        self.return_on_investment = 0
    

    def income(self):
        self.rental_income = int(input('What is your rental income?'))
        self.laundry = int(input('What is your laundry income?'))
        self.storage = int(input('What is your storage income?'))
        self.misc = int(input('What is your misc income?'))

        if self.rental_income >= 0:
            print(f"Your monthly rental income is {self.rental_income}")
        else:
            print("Invalid input, please try again.")

        if self.laundry >= 0:
            print(f"Your monthly laundry income is {self.laundry}")
        else:
            print("Invalid input, please try again.")

        if self.storage >= 0:
            print(f"Your monthly storage income is {self.storage}")
        else:
            print("Invalid input, please try again.")

        if self.misc >= 0:
            print(f"Your monthly storage income is {self.misc}")
        else:
            print("Invalid input, please try again.")

        self.total_monthly_income = self.rental_income + self.laundry + self.storage + self.misc
        print(f"The total monthly income is {self.total_monthly_income}")


    def expenses(self):
        self.taxes = int(input('How much is your taxes?'))
        self.insurance = int(input('How much is your insurance?'))
        self.water = int(input('How much is your water?'))
        self.garbage = int(input('How much is your garbage?'))
        self.electric = int(input('How much is your electricity?'))
        self.gas = int(input('How much is your gas?'))
        self.hoa_fees = int(input('How much is your hoa fees?'))
        self.lawn = int(input('How much is your lawncare?'))
        self.vacancy = int(input('How much is your vacancy?'))
        self.repairs = int(input('How much are your repairs?'))
        self.cap_ex = int(input('How much is your capital expenditure?'))
        self.property_management = int(input('How much is your property management?'))
        self.mortgage = int(input('How much is your mortgage?'))

        if self.taxes >= 0:
            print(f"Your monthly taxes is {self.taxes}")
        else:
            print("Invalid input, please try again.")

        if self.insurance >= 0:
            print(f"Your monthly insurance is {self.insurance}")
        else:
            print("Invalid input, please try again.")

        if self.water >= 0:
            print(f"Your monthly water is {self.water}")
        else:
            print("Invalid input, please try again.")

        if self.garbage >= 0:
            print(f"Your monthly garbage is {self.garbage}")
        else:
            print("Invalid input, please try again.")

        if self.electric >= 0:
            print(f"Your monthly electric is {self.electric}")
        else:
            print("Invalid input, please try again.")

        if self.gas >= 0:
            print(f"Your monthly gas is {self.gas}")
        else:
            print("Invalid input, please try again.")

        if self.hoa_fees >= 0:
            print(f"Your monthly hoa fee is {self.hoa_fees}")
        else:
            print("Invalid input, please try again.")

        if self.lawn >= 0:
            print(f"Your monthly lawn is {self.lawn}")
        else:
            print("Invalid input, please try again.")

        if self.vacancy >= 0:
            print(f"Your monthly vacancy is {self.vacancy}")
        else:
            print("Invalid input, please try again.")
        if self.repairs >= 0:
            print(f"Your monthly repair is {self.repairs}")
        else:
            print("Invalid input, please try again.")

        if self.cap_ex >= 0:
            print(f"Your monthly capital expenditure is {self.cap_ex}")
        else:
            print("Invalid input, please try again.")

        if self.property_management >= 0:
            print(f"Your monthly property management fee is {self.property_management}")
        else:
            print("Invalid input, please try again.")

        if self.mortgage >= 0:
            print(f"Your monthly mortgage is {self.mortgage}")
        else:
            print("Invalid input, please try again.")

        self.total_monthly_expenses = self.taxes + self.insurance + self.water + self.garbage + self.electric + self.gas + self.hoa_fees + self.lawn + self.vacancy + self.repairs + self.cap_ex + self.property_management + self.mortgage
        print(f"The total monthly expense is {self.total_monthly_expenses}")
    
    
    def cashflow(self):
        self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        print(f"The total monthly cash flow is {self.total_monthly_cash_flow}")

        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
        print(f"The total annual cash flow is {self.total_annual_cash_flow}")

    def investment(self):
        self.down_payment = int(input('How much is your down payment?'))
        self.closing_cost = int(input('How much is your closing costs?'))
        self.rehab_budget = int(input('How much is your rehab budget?'))
        self.misc_other = int(input('How much is your misc costs?'))  

        if self.down_payment >= 0:  
             print(f"Your down payment is {self.down_payment}")
        else:
            print("Invalid input, please try again.")

        if self.closing_cost >= 0:
            print(f"Your closing cost is {self.closing_cost}")
        else:
            print("Invalid input, please try again.")

        if self.rehab_budget >= 0:
            print(f"Your rehab budget is {self.rehab_budget}")
        else:
            print("Invalid input, please try again.")

        if self.misc_other >= 0:
            print(f"Your misc other is {self.misc_other}")
        else:
            print("Invalid input, please try again.")
        
        self.total_investment = self.down_payment + self.closing_cost + self.rehab_budget + self.misc_other
        print(f"Your total investment is {self.total_investment}")

        self.return_on_investment = (self.total_annual_cash_flow / self.total_investment) * 100
        print(f"The ROI is {self.return_on_investment} %")


    def UserInput(self):
        while True:
            response = input("Would you like to calculate your ROI? Yes, No").lower()
            if response == "yes":
                self.income()
                self.expenses()
                self.cashflow()
                self.investment()
            elif response == "no":
                print("Goodbye.")
                break
            else:
                print("Invalid input, please try again.")

                

test = Roi()
test.UserInput()







