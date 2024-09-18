import re
import unittest
from unittest.mock import patch
from io import StringIO

# The applicant's details and application status will be stored in database
# to avoid duplicate requests
database = {}
#Key in the database
application_id = 1

def welcome_message():
    """ Welcome message when the app starts
    Main menu of the app, user can either go to the application form or close the app
    """
    print("-------------------------")
    print(" Welcome to CheckAloan!\n"
          " Where you are not alone!")
    print("-------------------------")
    print("1. Fill out the loan application.")
    print("2. Close the application.")
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

def get_name():
    """
    Get the name of the user
    """
    try:
        while True:
            name = input("Please enter your full name:\n")
            # Check for digits in name
            name_check = re.findall('\\d', name)
            if name.strip() == "":
                print("The name field cannot be empty.")
            elif len(name) < 5:
                print("The name is too short.")
            elif name_check:
                print("Name cannot contain numbers.")
            else:
                break  # Exit loop if name is valid
    except IndexError as e:
        print(f"Wrong data was entered: {e}")
    return name
                
def get_email():
    """
    Get the contact phone number (10 digits)
    """
    email = input("Please provide your contact email address:\n")
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    while True:  
        if re.fullmatch(regex, email) is None:  
            print("The email provided is invalid")  
            email = input("Please enter a valid email address:\n")
        else:
            break  
    return email
        
def get_phone():
    """
    Get the contact phone number
    """
    phone = input("Please enter your 10-digit phone number:\n")
    pattern = re.compile(r'^\d{10}$')
    while True:
        if pattern.match(phone) is None:
            phone = input("Please enter a valid phone number:\n")
        else:
            break
    return phone
        
def get_age():
    """
    Get the age of the user
    """
    while True:
        try:
            age = int(input("How old are you?:\n"))
            if age < 18:
                print("You must be at least 18 years old to apply for a loan.\n"
                    "------------------------------------------------------------------\n"
                    "Application cancelled.")
                return False
            elif age > 18 and age < 65:
                return age
                break
            else:
                print("Sorry, you are too old to apply for a loan..\n"
                    "-------------------------------------------\n"
                    "Application cancelled.")
                return None
        except ValueError:
            print("Invalid input. Please enter a valid age.")
    
            
def get_marital_status():
    """
    Get the marital status of the user
    """
    while True:
        try:
             marital_status = input("What is your marital status(Married/Single)?:\n")
             if marital_status.upper() == "SINGLE":
                 marital_status = "Single"
                 break
             elif marital_status.upper() == "MARRIED":
                 marital_status = "Married"
                 break
             else:
                 print("Please enter either 'Married' or 'Single'.")
        except IndexError:
            print("No data was entered.")
    return marital_status
                        
def get_dependent_children():
    """
    Get the number of dependent kids
    """
    while True:
        try:
            children = int(input("Number of dependent kids:\n"))
            if children < 0:
                print("The number of kids cannot be negative. Pleaser enter 0 or a higher number.")
            else:
                break
        except ValueError as e:
            print(f"{e} is not a valid number.")
    return children
            
def get_employment_status():
    """
    Get the employment status of the user
    """
    while True:
        try:
            employment = input("Are you employed? Please enter 'y' for yes or 'n' for no:\n")
            if employment.capitalize()[0] == "Y":
                employment = True
                return employment
                break
            elif employment.capitalize()[0] == "N":
                employment = False
                print("Sorry, we cannot offer a loan if you are not employed.\n"
                      "-------------------------------------------------------\n"
                      "Application cancelled.")
                return False
            else:
                print("Please enter either y or n!")
        except IndexError:
            print("No data was entered.")
    
            
def get_income():
    """
    Get the income of the user.
    """
    while True:
        try:
            income = int(input("Please provide your monthly income:\n"))
            while income < 0:
                income = int("Income cannot be negative. Please enter a valid amount:\n")
            break
        except ValueError:
            print("Incorrect data was entered.")
    return income


def get_expense(income):
    """
    Monthly expenses including rent, utilities, food, and debt payments
    """
    while True:
        try:
            expense = int(input("Monthly expenses including rent, utilities, food, pet care and debt payments:\n"))
            if expense < 0:
                print("Expenses cannot be negative.")
            elif expense > income:
                print("Your expenses exceed your income. Loan request rejected.")
                return None
            else:
                return expense
        except ValueError as e:
            print(f"Incorrect data was entered: {e}")

def get_loan_amount():
    """
    Get the loan amount. Loan amount cannot exceed 20 000..
    """
    while True:
        try:
            loan_amount = int(
            input("How much would you like to borrow?\n"))
            if loan_amount > 20000:
                answer = input(
                            "Would you like to proceed with the maximum amount of 20 000?" 
                            "Enter 'yes' or 'no':\n")
                if answer.capitalize()[0] == "N":
                    print("-------------------------------------------")
                    print("Application cancelled!")
                    print("-------------------------------------------")
                    return None
                elif answer.capitalize()[0] == "Y":
                    loan_amount = 20000
                    return loan_amount
                    break
                else:
                    answer = input("Sorry, you have entered a wrong character. Enter y or n:\n")
                    while answer.capitalize()[0] != "Y" and answer.capitalize()[0] != "N":
                        answer = input("Sorry, you have entered a wrong character. Enter y or n:\n")
            elif loan_amount <= 0:
                print("Amount must be higher than 0.")
            else:
                return loan_amount
                break
        except (ValueError, IndexError) as e:
            print(f"Incorrect data was entered: {e}")
    

def get_monthly_payment(loan_amount):
    """
    Monthly payment of the loan. Maximum loan length is 5 years so the loan/payment cannot be more than 60.
    """
    while True:        
        try:
            monthly_payment = int(input("How much would you like to pay back monthly:\n"))
            if loan_amount/monthly_payment > 60:
                print("-------------------------------------------------")
                print("Sorry, the maximum loan term is 5 years.")
                print("-------------------------------------------------")
                print("Based on the entered details the loan length"
                            f" is {round(loan_amount/monthly_payment)}")
                print("-------------------------------------------------")
                print("Please enter higher monthly payment.")
                print("-------------------------------------------------")
            elif loan_amount < monthly_payment:
                print("The monthly payment cannot exceed the loan amount. Monthly payment must be less.")
            elif monthly_payment <=0 :
                print("The monthly payment must be greater than 0.")
            else:
                return monthly_payment
                break
        except (ValueError, ZeroDivisionError) as e:
            print(f"Incorrect data was entered: {e}")

def applicant_details():
    """
    Getting the details from the user
    """    
    while True:
        name = get_name()
        email = get_email()
        phone = get_phone()
        age = get_age()
        if not age:
            break  # Exit if age is under 18 or over 65)
        marital_status = get_marital_status()
        kids = get_dependent_children()
        employment = get_employment_status()
        if not employment:
            break  # Exit if not employed
        income = get_income()
        expense = get_expense(income)
        if expense is None:
            break  # Exit if expenses exceed income
        loan_amount = get_loan_amount()
        if not loan_amount:
            break  # Exit if loan amount is invalid or application is canceled
        monthly_payment = get_monthly_payment(loan_amount)
        return name, email, phone, age, marital_status, kids, employment, income, expense, loan_amount, monthly_payment

class Test(unittest.TestCase):
    """
    Testing the get functions
    """
    @patch('builtins.input', return_value = "Tamas")
    def test_get_name(self,mock_input):
        name = get_name()
        self.assertEqual(name,"Tamas")
        
    @patch('builtins.input', return_value = "tamasgavlider@gmail.com")
    def test_get_email(self,mock_input):
        email = get_email()
        self.assertEqual(email,"tamasgavlider@gmail.com")
        
    @patch('builtins.input', return_value = "1234567890")
    def test_get_phone(self,mock_input):
        phone = get_phone()
        self.assertEqual(phone,"1234567890")
        
    @patch('builtins.input', return_value = 30)
    def test_get_age(self,mock_input):
        age = get_age()
        self.assertEqual(age,30)
        
    @patch('builtins.input', return_value = "Married")
    def test_get_marital_status(self,mock_input):
        marital_status = get_marital_status()
        self.assertEqual(marital_status,"Married")
        
    @patch('builtins.input', return_value = 2)
    def test_get_dependent_kids(self,mock_input):
        kids = get_dependent_children()
        self.assertEqual(kids,2)
        
    # Test for an applicant who is employed   
    @patch('builtins.input', return_value = "y")
    def test_get_employment_status_employed(self,mock_input):
        employed_applicant = get_employment_status()
        self.assertTrue(employed_applicant,True)
        
    # Test for an applicant who is unemployed   
    @patch('builtins.input', return_value = "n")
    def test_get_employment_status_employed(self,mock_input):
        employed_applicant = get_employment_status()
        self.assertFalse(employed_applicant,False)
    
    @patch('builtins.input', return_value = 1000)
    def test_get_employment_status_employed(self,mock_input):
        income = get_income()
        self.assertEqual(income,1000)
        
    @patch('builtins.input', return_value = 450)
    def test_get_employment_status_employed(self,mock_input):
        expense = get_expense(1000)
        self.assertEqual(expense,450)   
    #Test for the expense if it is greater than income
    @patch('builtins.input', return_value = 500)
    def test_get_employment_status_employed(self,mock_input):
        expense = get_expense(400)
        self.assertEqual(expense,None)   
     
    @patch('builtins.input', return_value = 5000)
    def test_get_employment_status_employed(self,mock_input):
        loan_amount = get_loan_amount()
        self.assertEqual(loan_amount,5000)
    # Test for loan amount if user confirms the maximum loan amount
    @patch('builtins.input', side_effect=['25000', 'yes'])
    def test_loan_amount_exceeds_limit_proceed(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_loan_amount()
            self.assertEqual(result, 20000)
    # Test for loan amount if user want to borrow more than 20000 and cancellind the application
    @patch('builtins.input', side_effect=['25000', 'no'])
    def test_loan_amount_exceeds_limit_cancel(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_loan_amount()
            self.assertIsNone(result)
            self.assertIn("Application cancelled!", mock_stdout.getvalue())
    # Test if the loan amount is negative
    @patch('builtins.input', side_effect='-5000')
    def test_loan_amount_exceeds_limit_cancel(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_loan_amount()
            self.assertIn("Incorrect data was entered: invalid literal for int() with base 10:", mock_stdout.getvalue())
    
    @patch('builtins.input', return_value = 5000)
    def test_get_employment_status_employed(self,mock_input):
         monthly_payment = get_monthly_payment(10000)
         self.assertEqual(monthly_payment,5000)
   
    
#if __name__ == '__main__':
 #   unittest.main()

class Applicant:
    """
    Necessary details of the user based on the loan eligibility will be
    decided. It calculates the score and interest rate based on the provided
    details.Either approve or reject the loan and add the user to the database
    """

    def __init__(self, name, email, phone, age, marital_status, kids,
                 employment, income, expenses, loan_amount, monthly_payment):
        """
        General contact details and important details needed to make a decision.
        Score and interest rate have values. These will be modified based on the provided details.
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
        self.score = 0 # Max score is 130, under 50 the application will be rejected
        self.interest_rate = 1 # Interest rate depends on user details, calculated after the approval
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
                f"Number of kids: {self.kids}\n"
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
        self. name = get_name()

    def change_email(self):
        """
        Update the email address
        """
        self.email = get_email()
            
    def change_phone(self):
        """
        Update the phone number
        """
        self.phone = get_phone()

    def change_age(self):
        """
        Update the age
        """
        self.age = get_age()

    def change_marital_status(self):
        """
        Update marital status
        """
        if self.marital_status.capitalize()[0] == "S":
            self.marital_status = "Married"
        else:
            self.marital_status = "Single"

    def change_kids(self):
        """
        Update the number of dependent kids
        """
        self.kids = get_dependent_children()


    def change_employment_status(self):
        """
        Update employment status
        """
        if self.employment is True:
            self.employment = False
        else:
            self.employment = True
        

    def change_income(self):
        """
        Update income
        """
        
        try:
            self.income = int(input("Enter the correct income amount:\n"))
            while True:
                if self.income <=0:
                    print(("Income cannot be less or equal to 0:\n"))
                    self.income = int(input("Enter higher amount:\n"))
                elif self.income <= self.expenses:
                    print("Income cannot be less than the monthly expenses.")
                    self.income = int(input("Enter higher amount:\n"))
                else:
                    break
        except (ValueError, IndexError,ZeroDivisionError) as e:
            print(f"Wrong data was entered: {e}")

    def change_expense(self):
        """
        Update expenses
        """
        while True:
            try:
                self.expenses = int(input("Enter the monthly expenses:\n"))
                if self.expenses <=0: 
                    print("The expense cannot be less or equal to 0.")
                elif self.expenses > self.income:
                    print("The expense cannot be higher than the income.")
                else: 
                    break
            except (ValueError, IndexError,ZeroDivisionError) as e:
                print(f"Wrong data was entered: {e}")

    def change_loan(self):
        """
        Update loan amount
        """
        while True:
            try:
                self.loan_amount = int(input("Correct loan amount:\n"))
                if self.loan_amount > 20000:
                    print("The maximum amount is 20000. Please do not enter higher amount.")
                elif self.loan_amount <= self.monthly_payment:
                    print("The loan amount is less than or equal to the monthly payment.")
                elif self.loan_amount/self.monthly_payment > 60:
                    self.monthly_payment = round(self.loan_amount/60)
                    break
                else:
                    break
            except (ValueError, IndexError) as e:
                print(f"Wrong data was entered: {e}")
        

    def change_monthly_payment(self):
        """
        Update the monthly payment
        """
        while True:
            try:
                self.monthly_payment = int(input("Enter the updated estimated monthly payment:\n"))
                if self.loan_amount/self.monthly_payment > 60:
                    print("Sorry the loan lenght exceeds the maximum of 60 months.")
                elif self.loan_amount <= self.monthly_payment:
                    print("The monthly payment cannot exceed the loan amount. The monthly payment must be less.")
                elif self.monthly_payment <=0:
                    print("Amount cannot be 0 or less than 0.")
                else:
                    break
            except (ValueError,ZeroDivisionError) as e:
                print(f"Wrong data was entered: {e}")
        
    def make_changes(self):
        """
        Based on user input changes can be made on details or continue
        """
        print("-------------------------------------------\n")
   
        try:
            answer = input("The above details are correct? Press enter to submit your details  or 'n'"
                           " to make changes:\n")
            while True:
                    if answer.capitalize()[0] == "":
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
                            change = input("Please enter the number of the field that needs to be updated:\n")
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
                                print("Number out of range.")
                    else:
                        answer = input("Please press enter to submit for review or n to make changes.")
        except (ValueError,IndexError) as e:
                print(f"Wrong data was entered: {e}.") 
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

    def check_score_for_employment_status(self):
        """
        Score/Interest for employment status
        """
        if self.employment is False:
            self.score -= 130
        else:
            self.score += 130
            self.interest_rate += 0.01
        return self.score, self.interest_rate

    def calculate_monthly_payment(self):
        """
        Calculating the monthly payment with interest
        """
        return self.monthly_payment * self.interest_rate

    def decision(self):
        """
        Check the applicant score and approved/reject the loan request
        """
        return "APPROVED" if self.score > 50 else "REJECTED"

    def loan_details(self):
        """
        Loan details for approved applications
        """
        if self.decision() == "APPROVED":
            print("------------------------------------\n"
                  f" The approved loan amount is {self.loan_amount}\n"
                  f" The interest rate is {round((self.interest_rate-1)*100)}%\n"
                  f" The monthly payment is {round(self.monthly_payment*self.interest_rate)}\n"
                  "------------------------------------")
        elif self.decision() == "REJECTED":
            print("Unfortunately, your loan request cannot be approved based on the provided details.\n"
                  f"You have reached {self.score} points based on the provided details.\n"
                  "It is not sufficient for the loan approval.")

    def add_to_database(self):
        """
        Add the applicant's name to the database as the key
        the most important details of the application as values
        """
        global database, application_id
        database[application_id] = { "Name": self.name.upper(), "Email": self.email.upper(), "Score": self.score,
                               "Loan amount": self.loan_amount,
                               "Monthly payment": round(self.monthly_payment *
                               self.interest_rate),
                               "Application": self.decision()}
        application_id += 1
        return database
    
    def check_duplicates(self):
        global database
        for applicant_id, applicant in database.items():
            if applicant["Email"] == self.email.upper() and applicant["Name"] == self.name.upper():
                print(f"You have already applied for a loan, and it was {applicant['Application']}.\n"
                      f"{applicant}")
                return True
            
            else:
                self.add_to_database()
                return False
          

def run_app():
    while welcome_message():
        print("-----------------------------------------------")
        user = applicant_details()
        if user:
            applicant = Applicant(*user)
            print(applicant.summary())
            print(applicant.make_changes())
            print(applicant.summary())
            applicant.check_score_for_employment_status()
            applicant.check_score_for_age()
            applicant.check_score_for_cash_flow()
            applicant.check_score_for_kids()
            applicant.check_score_for_marital_status()
            applicant.calculate_monthly_payment()
            print("The application is being reviewed.")
            print("------------------------------------")
            if applicant.check_duplicates():
                print("------------------------------------")
            else:
                print(applicant.decision())
                applicant.loan_details()
                applicant.add_to_database()
                print("------------------------------------")
                print("Your application has been saved.")
            print("------------------------------------")
            print("Thank you for choosing CheckAloan.")
            print("Returning to the main menu.")
            print("------------------------------------")
        else:
            print("Application is closing...")

run_app()