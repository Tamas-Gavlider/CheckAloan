def welcome_message():
    """ Welcome message when the app starts """
    print("-------------------------")
    print(" Welcome to CheckAloan!\n"
          " Where you are not alone!")
    print("-------------------------")


# The applicant's email and application status will be stored in database
# to avoid duplicate requests
database = {}


class Applicant:
    """
    Necessary details of the applicant based on the loan eligibility will be
    decided. It calculates the score and interest rate based on the provided
    details.Either approve or reject the loan and add the user to the database
    """

    def __init__(self, name, email, phone, age, marital_status, kids,
                 employment, income, expenses, loan_amount, monthly_payment):
        """
        General contact details and important details which needed to make
        decision. Score and interest rate have values.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.marital_status = marital_status
        self.kids = kids
        self.employment = employment
        self.income = income
        self.expenses = expenses
        self.loan_amount = loan_amount
        self.monthly_payment = monthly_payment
        self.score = 0
        self.interest_rate = 1

    def summary(self):
        """
        Summary of the provided details
        """
        return ("---------------------------------------------------\n"
                f"Name: {self.name}!\n"
                f"Email: {self.email}\n"
                f"Phone number: {self.phone}\n"
                f"Age: {self.age}\n"
                f"Marital status: {self.marital_status}\n"
                f"Kids: {self.kids}\n"
                f"Employment status: {self.employment}\n"
                f"Monthly income: {self.income}\n"
                f"Monthly expense: {self.expenses}\n"
                f"Loan amount: {self.loan_amount}\n"
                f"Monthly payment: {self.monthly_payment}\n"
                "-------------------------------------------")

    def change_name(self):
        """
        Update the name
        """
        self.name = input("Please enter the correct name:\n")
        while self.name == "" or len(self.name) < 5:
            self.name = input("Please enter a valid name:\n")
        

    def change_email(self):
        """
        Update the email address
        """
        self.email = input("Enter the correct email address:\n")
        while "@" not in self.email and "." not in self.email:
             self.email = input("Please enter a valid email address:\n")
            
    def change_phone(self):
        """
        Update the phone number
        """
        self.phone = input("Enter the correct phone number:\n")
        while len(self.phone) != 10:
            self.phone = input("Please enter a valid phone number:\n")

    def change_age(self):
        """
        Update the age
        """
        try:
            self.age = int(input("Enter your correct age:\n"))
            if self.age < 18:
                print("Sorry we cannot approve the credit if you are under 18.")
                return False
        except (ValueError, IndexError):
            print("Wrong data was entered.")

    def change_marital_status(self):
        """
        Update marital status
        """
        if self.marital_status.capitalize()[0] == "S":
            self.marital_status = "Married"

    def change_kids(self):
        """
        Update the number of dependent kids
        """
        try:
            self.kids = int(input("Please enter the number of dependent kids:\n"))
        except ValueError:
            print("Wrong data was entered.")

    def change_employment_status(self):
        """
        Update employment status
        """
        if self.employment is True:
            self.employment = False

    def change_income(self):
        """
        Update income
        """
        try:
            self.income = int(input("Enter the correct income amount:\n"))
        except (ValueError, IndexError):
            print("Wrong data was entered.")

    def change_expense(self):
        """
        Update expenses
        """
        try:
            self.expenses = int(input("Enter the monthly expenses:\n"))
        except (ValueError, IndexError):
            print("Wrong data was entered.")

    def change_loan(self):
        """
        Update loan amount
        """
        try:
            self.loan_amount = int(input("Correct loan amount:\n"))
            while self.loan_amount < self.monthly_payment and self.loan_amount > 20000:
                if self.loan_amount > 20000:
                    self.loan_amount = int(input("The maximum amount is 20000. Please do not enter higher amount:\n"))
                elif self.loan_amount < self.monthly_payment:
                    self.loan_amount = int(input("The loan amount is less than the monthly payment."
                                                        "Enter higher amount:\n"))
        except ValueError:
            print("Wrong data was entered.")
        

    def change_monthly_payment(self):
        """
        Update the monthly payment
        """
        self.monthly_payment = int(
            input("Enter the updated estimated monthly payment:\n"))
        while self.monthly_payment > self.loan_amount or self.loan_amount/self.monthly_payment > 60:
            try:
                if self.loan_amount/self.monthly_payment > 60:
                    print("Sorry the loan lenght exceeds the maximum of 60 months.")
                    self.monthly_payment = int(input("Enter the updated estimated monthly payment:\n"))
                elif self.loan_amount < self.monthly_payment:
                    self.monthly_payment = int(input("The monthly payment cannot exceed the loan amount. The monthly payment must be less:\n"))
            except ValueError:
                print("Wrong data was entered.")
        
    def make_changes(self):
        """
        Based on user input changes can be made on details or continue
        """
        print("-------------------------------------------\n")
        answer = input(
            "The above details are correct? y/n:\n")
        while True:
            try:
                if answer.capitalize()[0] == "Y":
                    print("Thank you for the confirmation. Now we are checking"
                          " if you are eligible for a loan...")
                    break
                elif answer.capitalize()[0] == "N":
                    print(f"1. Name: {self.name}\n"
                          f"2. Email: {self.email}\n"
                          f"3. Phone: {self.phone}\n"
                          f"4. Age: {self.age}\n"
                          f"5. Marital status: {self.marital_status}\n"
                          f"6. Kids: {self.kids}\n"
                          f"7. Employment status: {self.employment}\n"
                          f"8. Income: {self.income}\n"
                          f"9. Expenses: {self.expenses}\n"
                          f"10. Loan amount: {self.loan_amount}\n"
                          f"11. Monthly payment: {self.monthly_payment}\n"
                          "12. Confirm details\n"
                          "-------------------------------------")
                    change = input("Please enter the number of the row that"
                                   " needs to be updated:\n")
                    if change == '1':
                        self.change_name()
                    elif change == '2':
                        self.change_email()
                    elif change == "3":
                        self.change_phone()
                    elif change == "4":
                        self.change_age()
                    elif change == "5":
                        self.change_marital_status()
                    elif change == "6":
                        self.change_kids()
                    elif change == "7":
                        self.change_employment_status()
                    elif change == "8":
                        self.change_income()
                    elif change == "9":
                        self.change_expense()
                    elif change == "10":
                        self.change_loan()
                    elif change == "11":
                        self.change_monthly_payment()
                    elif change == "12":
                        break
                    else:
                        print("Number out of range. Entere a number between 1-12")
                else:
                    print("Please enter y or n.")
            except ValueError:
                print("Wrong data was entered.")
        return self.summary()

    def check_score_for_age(self):
        """
        Calculate the score/interest for the age of the applicant
        """
        if self.age < 18:
            self.score -= 130
        elif self.age < 25 and self.age > 18:
            self.score += 10
            self.interest_rate += 0.02
        elif self.age >= 25 and self.age < 60:
            self.score += 20
            self.interest_rate += 0.01
        else:
            self.score += 0
            self.interest_rate += 0.03
        return self.score, self.interest_rate

    def check_score_for_cash_flow(self):
        """
        Calculate score/interest based on the income,expense considering the monthly payment for the request loan
        """
        if self.expenses > self.income:
            self.score -= 100
        elif self.income > self.expenses:
            if self.income - self.expenses > self.monthly_payment*2:
                self.score += 30
                self.interest_rate += 0.01
            elif self.income - self.expenses >= self.monthly_payment*1.5:
                self.score += 20
                self.interest_rate += 0.02
            else:
                self.score += 0
                self.interest_rate += 0.03
        else:
            self.score += 0
        return self.score, self.interest_rate

    def check_score_for_marital_status(self):
        """
        Score/Interest for the marital status
        """
        if self.marital_status.capitalize()[0] == "M":
            self.score += 20
            self.interest_rate += 0.01
        else:
            self.score += 10
            self.interest_rate += 0.02
        return self.score, self.interest_rate

    def check_score_for_kids(self):
        """
        Score/Interest based on the number of kids
        """
        if self.kids == 0:
            self.score += 30
            self.interest_rate += 0.01
        elif self.kids > 0 and self.kids < 3:
            self.score += 20
            self.interest_rate += 0.02
        else:
            self.score += 10
            self.interest_rate += 0.03
        return self.score, self.interest_rate

    def employment_status(self):
        """
        Score/Interest for employment status
        """
        if self.employment:
            self.score += 30
            self.interest_rate += 0.01
        else:
            self.score -= 130
        return self.score, self.interest_rate

    def calculate_monthly_payment(self):
        """
        Calculating the monthly payment with interest
        """
        self.monthly_payment *= self.interest_rate
        return self.monthly_payment

    def decision(self):
        """
        Check the applicant score and approved/reject the loan request
        """
        return "Approved" if self.score > 50 else "Rejected"

    def loan_details(self):
        """
        Loan details for approved applications
        """
        if self.decision() == "Approved":
            print("------------------------------------\n"
                  f" The approved loan amount is {self.loan_amount}\n"
                  f" The interest rate is {round((self.interest_rate-1)*100)}%\n"
                  f" The monthly payment is {round(self.monthly_payment*self.interest_rate)}\n"
                  "------------------------------------")
        else:
            print("Unfortunately, your loan request cannot be approved based on the provided details.\n"
                  f"You have reached {self.score} points based on the provided details.\n"
                  "It is not sufficient for the loan approval.")

    def add_to_database(self):
        """
        Add the applicant's email to database as key and the applications status as value
        """
        database[self.name] = {'Email': self.email, 'Score': self.score,
                               'Loan amount': self.loan_amount,
                               "Monthly payment": self.monthly_payment *
                               self.interest_rate,
                               "Application": self.decision()}
        return database


def applicant_details():
    """
    Getting the details from the applicant and validate inputs
    """
    name = input("Please provide your full name:\n")
    while name == "" or len(name) < 5:
        name = input("Please enter a valid name:\n")
    email = input("Please provide your contact email address:\n")
    while "@" not in email or "." not in email:
        email = input("Please enter a valid email address:\n")
    phone = input("Please provide your contact phone number:\n")
    while len(phone) > 10 or len(phone) < 10:
        phone = input("Please enter a valid phone number:\n")
    while True:
        try:
            age = int(input("How old are you?:\n"))
            if age < 18:
                print("You cannot apply for a loan. You must be at least 18 years old.\n"
                    "------------------------------------------------------------------\n"
                    "Application cancelled.")
                return False
            elif age > 18 and age < 65:
                break
            else:
                print("Sorry you are too old to apply for a loan.\n"
                    "-------------------------------------------\n"
                    "Application cancelled.")
                return False
        except ValueError:
            print("Wrong data entered")
    marital_status = input("What is your marital status(Married/Single)?:\n")
    while marital_status.capitalize()[0] != "M" and marital_status.capitalize()[0] != "S":
        marital_status = input("Please enter either married or single:\n")
    if marital_status.capitalize()[0] == "Y":
        marital_status = "Married"
    else:
        marital_status = "Single"
    while True:
        try:
            kids = int(input("Number of dependent kids:\n"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            employment = input("Are you employed?:\n")
            if employment.capitalize()[0] == "Y":
                employment = True
                break
            elif employment.capitalize()[0] == "N":
                employment = False
                print("Sorry we cannot offer any loan if you are not employed\n"
                      "-------------------------------------------------------\n"
                      "Application cancelled.")
                return False
            else:
                print("Please enter either yes or no!")
        except IndexError:
            print("No data was entered.")
    while True:
        try:
            income = int(input("Monthly income:\n"))
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            expense = int(input(
                "Monthly expenses including rent, utilities, food, pet care and debt payments:\n"))
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            loan_amount = int(
                input("How much money would you like to borrow?:\n"))
            if loan_amount > 20000:
                answer = input(
                    "Sorry the request amount is too high. The maximum amount is 20000. Would you "
                    "like to proceed with the max amount? y/n:\n")
                if answer.capitalize()[0] == "N":
                    print("-------------------------------------------")
                    print("Application cancelled!")
                    print("-------------------------------------------")
                    return False
                elif answer.capitalize()[0] == "Y":
                    loan_amount = 20000
                else:
                    answer = input("Sorry, you have entered a wrong character. Enter y or n:\n")
                    while answer.capitalize()[0] != "Y" or answer.capitalize()[0] != "N":
                        answer = input("Sorry, you have entered a wrong character. Enter y or n:\n")
            else:
                break
            break
        except (ValueError, IndexError):
            print("Incorrect data was entered.")
    monthly_payment = int(
                input("How much would you like to pay back monthly:\n"))
    while loan_amount/monthly_payment > 60 or loan_amount < monthly_payment:
        try:
            if loan_amount/monthly_payment > 60:
                print("-------------------------------------------------")
                print("Sorry the maximum length of the loan is 5 years.")
                print("-------------------------------------------------")
                print("Based on the entered details the loan length"
                      f" is {round(loan_amount/monthly_payment)}")
                print("-------------------------------------------------")
                monthly_payment = int(
                    input("Please enter higher monthly payment:\n"))
                print("-------------------------------------------------")
            elif loan_amount < monthly_payment:
                monthly_payment = int(
                    input("The monthly payment cannot be higher than the loan amount. Monthly payment must be less:\n"))
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            print("Incorrect data was entered.")

    return name, email, phone, age, marital_status, kids, employment, income, expense, loan_amount, monthly_payment


def main_menu():
    """
    Main menu of the app, user can either go to the application form or close the app
    """
    print("1. Fill out the loan application.")
    print("2. Closed the application.")
    print("-----------------------------------------------")
    choice = input("Please press 1 to start the loan application or 2 to quit:\n")
    while choice != "1" or choice != "2":
        if choice == "1":
            return True
        elif choice == "2":
            print("Application is closing...")
            return False
        else:
            choice = input("Please enter either 1 or 2:\n")


def run_app():
    welcome_message()
    while main_menu():
        print("-----------------------------------------------")
        user = applicant_details()
        if user:
            applicant = Applicant(*user)
            print(applicant.summary())
            print(applicant.make_changes())
            applicant.employment_status()
            applicant.check_score_for_age()
            applicant.check_score_for_cash_flow()
            applicant.check_score_for_kids()
            applicant.check_score_for_marital_status()
            applicant.calculate_monthly_payment()
            print("The application is being reviewed...")
            print("------------------------------------")
            print(applicant.decision())
            applicant.loan_details()
            applicant.add_to_database()
            print("------------------------------------")
            print("You application have been saved.")
            print("------------------------------------")
            print("Thank you for choosing CheckAloan.")
            print("Returning to main menu.")
            print("-----------------------------------------")
        else:
            print("Application is closing...")


run_app()
