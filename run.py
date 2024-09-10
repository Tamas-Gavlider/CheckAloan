welcome_message = "CheckAloan"

def applicant_details():
    """
   Getting the details from the applicant
    """
    name = input("Please provide your full name: ")
    email = input("Please provide your contact email address: ")
    phone = int(input("Please provide your contact phone number: "))
    age = int(input("How old are you?: "))
    marital_status = input("What is your marital status(Married/Single)?: ")
    kids = int(input("Number of dependent kids: "))
    income = int(input("Monthly income: "))
    expense = int(input("Monthly expenses including rent, utilities, food, pet care and debt payments: "))
    return name,email,phone,age,marital_status,kids,income,expense

class Applicant:
    """
    Necessary etails of the applicant based on the loan eligibility will be decided
    """
    def __init__(self,name,email,phone,age,marital_status,kids,income,expenses):
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age
        self.marital_status = marital_status
        self.kids = kids
        self.income = income
        self.expenses = expenses
    
    def summary(self):
        """
        Summary of the provided details
        """
        return (f"Hello {self.name}!"
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

def applicant_details():
    """
   Getting the details from the applicant
    """
    name = input("Please provide your full name: ")
    email = input("Please provide your contact email address: ")
    phone = int(input("Please provide your contact phone number: "))
    age = int(input("How old are you?: "))
    marital_status = input("What is your marital status(Married/Single)?: ")
    kids = int(input("Number of dependent kids: "))
    income = int(input("Monthly income: "))
    expense = int(input("Monthly expenses including rent, utilities, food, pet care and debt payments: "))
    return Applicant(name,email,phone,age,marital_status,kids,income,expense)



#test = Applicant('tamas','gavlider','2312@321.com',1234567890,35,'married',2,2500,1850)
#test.summary()
#a = test.make_changes()
#if( a[-1] == "c"):
#    print("Change details")
#else: 
#    print("Continue")

            
