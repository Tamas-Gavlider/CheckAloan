welcome_message = "CheckAloan"

class Applicant:
    """
    Necessary etails of the applicant based on the loan eligibility will be decided
    """
    def __init__(self,first_name,last_name,email,phone,age,marital_status,kids,income,expenses):
        self.first_name = first_name
        self.last_name = last_name
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
        return (f"Hello {self.first_name} {self.last_name}!"
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


test = Applicant('tamas','gavlider','2312@321.com',1234567890,35,'married',2,2500,1850)
test.summary()
a = test.make_changes()
if( a[-1] == "c"):
    print("Change details")
else: 
    print("Continue")

            
