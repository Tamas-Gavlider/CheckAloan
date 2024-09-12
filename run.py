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
    Necessary details of the applicant based on the loan eligibility will be decided
    """

    def __init__(self, name, email, phone, age, marital_status, kids, employment, income, expenses, loan_amount, monthly_payment):
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
        return ("-------------------------------------------\n"
                f"Hello {self.name}!\n"
                f"Please check if the details below are correct:\n"
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

    def make_changes(self):
        """
        Based on user input changes can be made on details or continue
        """
        answer = input(
            "To make any changes on the details above enter c and press enter,else enter s and press enter: ")
        return answer
    
    def check_score_for_age(self):
        """
        Calculate the score/interest for the age of the applicant
        """
        if self.age < 18:
            self.score -= 100
        elif self.age < 25 or self.age > 18:
            self.score += 10
            self.interest_rate += 0.02
        elif self.age >= 25 or self.age < 60:
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
            self.score -= 100
        return self.score, self.interest_rate

    def calculate_monthly_payment(self):
        """
        Calculating the monthly payment with interest 
        """
        self.monthly_payment *= self.interest_rate
        return self.monthly_payment

    def add_to_database(self):
        """
        Add the applicant's email to database as key and the applications status as value
        """
        database[self.name] = {'email' : self.email, 'score' : self.score, 'loan amount' : self.loan_amount}
        return database


def applicant_details():
    """
    Getting the details from the applicant and validate inputs
    """
    name = input("Please provide your full name: ")
    while name == "" or len(name) < 5:
        name = input("Please enter a valid name: ")
    email = input("Please provide your contact email address: ")
    while "@" not in email or "." not in email:
        email = input("Please enter a valid email address: ")
    phone = input("Please provide your contact phone number: ")
    while len(phone) > 10 or len(phone) < 10:
        phone = input("Please enter a valid phone number: ")
    age = int(input("How old are you?: "))
    while True:
        if age < 18:
            print("You cannot apply for a loan. You must be at least 18 years old.")
            break
        elif age > 18 and age < 65:
            break
        else:
            print("Sorry you are too old to apply for a loan.")
            break
    marital_status = input("What is your marital status(Married/Single)?: ")
    while marital_status.capitalize()[0] != "M" and marital_status.capitalize()[0] != "S":
        marital_status = input("Please enter either married or single: ")
    if marital_status.capitalize()[0] == "Y":
        marital_status = "Married"
    else:
        marital_status = "Single"
    while True:
        try:
            kids = int(input("Number of dependent kids: "))
            break
        except ValueError:
            print("Please enter a valid number. ")
    while True:
        try:
            employment = input("Are you employed?: ")
            if employment.capitalize()[0] == "Y":
                employment = True
                break
            elif employment.capitalize()[0] == "N":
                employment = False
                break
            else:
                print("Please enter either yes or no!")      
        except IndexError:
            print("No data was entered.") 
    while True:
        try:
            income = int(input("Monthly income: "))
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            expense = int(input(
                "Monthly expenses including rent, utilities, food, pet care and debt payments: "))
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            loan_amount = int(
                input("How much money would you like to borrow?: "))
            if loan_amount > 20000:
                answer = input(
                    "Sorry the request amount is too high. The maximum amount is 20000. Would you like to proceed with the max amount? y/n :")
                if answer.capitalize()[0] == "N":
                    print("-------------------------------------------")
                    print("Application cancelled!")
                    print("-------------------------------------------")
                    return False
                elif answer.capitalize()[0] == "Y":
                    loan_amount = 20000
                else:
                    print("Sorry, you have entered a wrong character. Enter y or n.")
            else:
                break
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            monthly_payment = int(
                input("How much would you like to pay back monthly: "))
            while loan_amount/monthly_payment > 60:
                print("-------------------------------------------")
                print("Sorry the maximum length of the loan is 5 years.")
                print("-------------------------------------------")
                print(f"Based on the entered details the loan length is {round(loan_amount/monthly_payment)}")
                print("-------------------------------------------")
                monthly_payment = int(input("Please enter higher monthly payment: "))
                print("-------------------------------------------")
        except (ValueError,ZeroDivisionError,UnboundLocalError):
            print("Incorrect data was entered.")
        break
        

    return name, email, phone, age, marital_status, kids, employment, income, expense, loan_amount, monthly_payment
    
    

def run_app():
    welcome_message()
    user = applicant_details()
    if user:
        applicant = Applicant(*user)
        print(applicant.summary())
        applicant.check_score_for_age()
        applicant.check_score_for_cash_flow()
        applicant.check_score_for_kids()
        applicant.check_score_for_marital_status()
        applicant.calculate_monthly_payment()
        print(applicant.score)
        print(applicant.interest_rate)
        print(applicant.monthly_payment)
        applicant.add_to_database()



run_app()