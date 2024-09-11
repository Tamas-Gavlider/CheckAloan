def welcome_message():
    """ Welcome message when the app starts """
    print("-------------------------")
    print(" Welcome to CheckAloan!\n"
          " Where you are not alone!")
    print("-------------------------")



# The applicant's email and application status will be stored in database 
# to avoid duplicate requests

database = {}
# Based on the provided details the applicant will receive points.
# If the score is high enough the application will be approved, if too low it will be auto rejected.
score = 0

class Applicant:
    """
    Necessary etails of the applicant based on the loan eligibility will be decided
    """

    def __init__(self, name, email, phone, age, marital_status, kids, income, expenses, loan_amount, monthly_payment):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.marital_status = marital_status
        self.kids = kids
        self.income = income
        self.expenses = expenses
        self.loan_amount = loan_amount
        self.monthly_payment = monthly_payment

    def summary(self):
        """
        Summary of the provided details
        """
        return ("-------------------------------------------"
                f"Hello {self.name}!\n"
                f"Please check if the details below are correct:\n"
                f"Email: {self.email}\n"
                f"Phone number: {self.phone}\n"
                f"Age: {self.age}\n"
                f"Marital status: {self.marital_status}\n"
                f"Kids: {self.kids}\n"
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

    def decision(self):
        if self.income - self.expenses > self.monthly_payment * 2:
            return "approved"
        elif self.income - self.expenses < self.monthly_payment*2:
            return "the requested amount cannot be approved"
        else:
            return "rejected"

    def add_to_database(self):
        """
        Add the applicant's email to database as key and the applications status as value
        """
        database[self.email] = self.decision()
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
    while True:
        try:
            kids = int(input("Number of dependent kids: "))
            break
        except ValueError:
            print("Please enter a valid number. ")
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
                    loan_amount = 0
                elif answer.capitalize()[0] == "Y":
                    loan_amount = 20000
                    break
                else:
                    print("Sorry, you have entered a wrong character. Enter y or n.")
            else:
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
        except ValueError:
            print("Incorrect data was entered.")
        break
        

    return name, email, phone, age, marital_status, kids, income, expense, loan_amount, monthly_payment

def check_score_for_age(age):
    """
    Calculate the score for the age of the applicant
    """
    if age < 25 or age > 18:
        score += 10
    elif age >= 25 or age < 60:
        score += 20
    else:
        score += 0
    return score
            
def check_score_for_cash_flow(income, expense,monthly_payment):
    """
    Calculate score based on the income,expense considering the monthly payment for the request loan
    """
    if expense > income:
        score += 0
    elif income > expense:
        if income - expense > monthly_payment*2:
            score += 30
        elif income - expense > monthly_payment:
            score += 10
        else:
            score += 0
    else:
        score += 0
    return score

def check_score_for_marital_status(marital_status):
    """
    Score for the marital status
    """
    if marital_status.capitalize()[0] == "Y":
        score += 20
    else:
        score += 10
    return score

def check_score_for_kids(kids):
    """
    Score based on the number of kids
    """
    if kids == 0:
        score += 30
    elif kids > 0 and kids < 3:
        score += 10
    else:
        score +=0
    return score

def calculate_monthly_payment(loan_amount,monthly_payment):
    """
    Calculating the monthly payment with interest 
    """
    interest = 1.1
    
    

user = applicant_details()
new_applicant = Applicant(*user)

print(new_applicant.summary())

# applicant_details()
