import unittest
from unittest.mock import patch
from io import StringIO
from run import *

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
    def test_get_employment_status_unemployed(self,mock_input):
        employed_applicant = get_employment_status()
        self.assertFalse(employed_applicant,False)
    
    @patch('builtins.input', return_value = 1000)
    def test_get_income(self,mock_input):
        income = get_income()
        self.assertEqual(income,1000)
        
    @patch('builtins.input', return_value = 450)
    def test_get_expenses(self,mock_input):
        expense = get_expense(1000)
        self.assertEqual(expense,450)   
    #Test for the expense if it is greater than income
    @patch('builtins.input', return_value = 500)
    def test_get_expenses_greater_than_income(self,mock_input):
        expense = get_expense(400)
        self.assertEqual(expense,None)   
     
    @patch('builtins.input', return_value = 5000)
    def test_get_loan_amount(self,mock_input):
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
    def test_loan_amount_negative(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = get_loan_amount()
            self.assertIn("Incorrect data was entered: invalid literal for int() with base 10:", mock_stdout.getvalue())
    
    @patch('builtins.input', return_value = 5000)
    def test_get_motnhly_payment(self,mock_input):
         monthly_payment = get_monthly_payment(10000)
         self.assertEqual(monthly_payment,5000)
   
    
if __name__ == '__main__':
    unittest.main()