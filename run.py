welcome_message = ("Welcome to CheckAloan!\n"
                   "Where you are not alone!\n")

# The applicant's email and application status will be stored in database to avoid duplicate requests
database = {}

class Applicant:
    """
    Necessary etails of the applicant based on the loan eligibility will be decided
    """
    def __init__(self,name,email,phone,age,marital_status,kids,income,expenses,loan_amount,monthly_payment):
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
        return (f"Hello {self.name}!\n"
        f"Please check if the details below are correct:\n"
        f"Email: {self.email}\n"
        f"Phone number: {self.phone}\n"
        f"Age: {self.age}\n"
        f"Marital status: {self.marital_status}\n"
        f"Kids: {self.kids}\n"
        f"Monthly income: {self.income}\n"
        f"Monthly expense: {self.expenses}\n")

    def make_changes(self):
        """
        Based on user input changes can be made on details or continue
        """
        answer = input("To make any changes on the details above enter c and press enter,else enter s and press enter: ")
        return answer
    
    def decision(self):
        if self.income - self.expenses > monthly_payment*2:
            return "approved"
        elif self.income - self.expenses < monthly_payment*2:
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
    while name == "" or len(name) < 4:
        name = input("Please enter a valid name: ")
    email = input("Please provide your contact email address: ")
    while "@" not in email or "." not in email:
        email = input("Please enter a valid email address: ")
    phone = int(input("Please provide your contact phone number: "))
    while phone > 9999999999 or phone < 1000000000:
        phone = int(input("Please enter a valid phone number: "))
    age = int(input("How old are you?: "))
    while True:
        if age < 18: 
            print("You cannot apply for a loan. You must be at least 18 years old.")
            return False
        elif age > 18 and age < 65:
            break
        else:
            print("Sorry you are too old to apply for a loan.")
            return False
    marital_status = input("What is your marital status(Married/Single)?: ")
    while marital_status.capitalize()[0] != "M" and marital_status.capitalize()[0] != "S":
        marital_status = input("Please enter either married or single:")
    while True:
        try:
            kids = int(input("Number of dependent kids: "))
            break
        except ValueError:
            print("Please enter a valid number: ")
    while True:
        try:
            income = int(input("Monthly income: "))
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            expense = int(input("Monthly expenses including rent, utilities, food, pet care and debt payments: "))
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            loan_amount = int(input("How much money would you like to borrow?: "))
            if loan_amount > 20000:
                answer = input("Sorry the request amount is too high. The maximum amount is 20000. Would you like to proceed with the max amoutn? y/n :")
                if answer.capitalize()[0] == "N":
                    return False
                else:
                    continue
            break
        except ValueError:
            print("Incorrect data was entered.")
    while True:
        try:
            monthly_payment = int(input("How much would you like to pay back monthly: "))
            break
        except ValueError:
            print("Incorrect data was entered.")
        
        
    return name,email,phone,age,marital_status,kids,income,expense,loan_amount,monthly_payment



#user = applicant_details()
#new_applicant = Applicant(user)

#test = Applicant('tamas gavlider','2312@321.com',1234567890,35,'married',2,2500,1850)
#print(test.summary())
applicant_details()

    
            
