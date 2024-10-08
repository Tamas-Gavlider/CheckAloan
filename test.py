import unittest
from unittest.mock import patch
from io import StringIO
from run import get_age, get_dependent_children, get_email,\
        get_employment_status, get_expense, get_income, get_loan_amount,\
        get_marital_status, get_monthly_payment, get_name, get_phone


class Test(unittest.TestCase):
    """
    Testing the get functions
    """
    # Test for name
    @patch("builtins.input", return_value="Tamas G")
    def test_get_name(self, mock_input):
        name = get_name()
        self.assertEqual(name, "Tamas G")

    # Test for the length of the name
    @patch("builtins.input", side_effect=["four", "Tamas G"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_name_short_input(self, mock_stdout, mock_input):
        name = get_name()
        output = mock_stdout.getvalue()
        self.assertEqual(name, "Tamas G")
        self.assertIn("The name is too short.", output)

    # Test if the name contains numbers
    @patch("builtins.input", side_effect=["1234335", "Tamas G"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_name_num_input(self, mock_stdout, mock_input):
        name = get_name()
        output = mock_stdout.getvalue()
        self.assertEqual(name, "Tamas G")
        self.assertIn("Name cannot contain numbers or"
                      " special characters.", output)

    # Test if no data entered
    @patch("builtins.input", side_effect=["", " ", "Tamas G"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_name_no_input(self, mock_stdout, mock_input):
        name = get_name()
        output = mock_stdout.getvalue()
        self.assertEqual(name, "Tamas G")
        self.assertIn("The name field cannot be empty.", output)

    # Test for email
    @patch("builtins.input", return_value="tamasgavlider@gmail.com")
    def test_get_email(self, mock_input):
        email = get_email()
        self.assertEqual(email, "tamasgavlider@gmail.com")

    # Test for invalid email
    @patch("builtins.input", side_effect=["twentyfive", "    ", "", "33",
                                          "12@.cmm", "123@gmail.com"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_email_wrong_input(self, mock_stdout, mock_input):
        email = get_email()
        output = mock_stdout.getvalue()
        self.assertEqual(email, "123@gmail.com")
        self.assertIn("The email provided is invalid", output)

    # Test for phone
    @patch("builtins.input", return_value="1234567890")
    def test_get_phone(self, mock_input):
        phone = get_phone()
        self.assertEqual(phone, "1234567890")

    # Test for invalid phone number
    @patch("builtins.input", side_effect=["twentyfive", "    ", "33",
                                          "1234567890"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_phone_invalid_input(self, mock_stdout, mock_input):
        phone = get_phone()
        output = mock_stdout.getvalue()
        self.assertEqual(phone, "1234567890")
        self.assertIn("Please enter a valid phone number.", output)

    # Test for age
    @patch("builtins.input", return_value=30)
    def test_get_age(self, mock_input):
        age = get_age()
        self.assertEqual(age, 30)

    # Test age if age > 65
    @patch("builtins.input", return_value=67)
    def test_get_age_over_65(self, mock_input):
        age = get_age()
        self.assertEqual(age, False)

    # Test age if age < 18
    @patch("builtins.input", return_value=17)
    def test_get_age_under_18(self, mock_input):
        age = get_age()
        self.assertEqual(age, False)

    # Test age for string and no inputs
    @patch("builtins.input", side_effect=["twentyfive", "", " ", "33"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_age_wrong_input(self, mock_stdout, mock_input):
        age = get_age()
        output = mock_stdout.getvalue()
        self.assertEqual(age, 33)
        self.assertIn("Invalid input. Please enter a valid age.", output)

    # Test for marital status - married
    @patch("builtins.input", return_value="Married")
    def test_get_marital_status(self, mock_input):
        marital_status = get_marital_status()
        self.assertEqual(marital_status, "Married")

    # Test for marital status - single
    @patch("builtins.input", return_value="Single")
    def test_get_marital_status_single(self, mock_input):
        marital_status = get_marital_status()
        self.assertEqual(marital_status, "Single")

    # Test marital status for wrong inputs
    @patch('builtins.input', side_effect=["sing", "", "33", "m", "Married"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_marital_status_wrong_input(self, mock_stdout, mock_input):
        marital_status = get_marital_status()
        output = mock_stdout.getvalue()
        self.assertEqual(marital_status, "Married")
        self.assertIn("Please enter either 'Married' or 'Single'.", output)

    # Test for dependent kids
    @patch("builtins.input", return_value=2)
    def test_get_dependent_kids(self, mock_input):
        kids = get_dependent_children()
        self.assertEqual(kids, 2)

    # Test dependent kids for wrong input
    @patch('builtins.input', side_effect=["s", "", "-1", " ", "0"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_dependent_kids_wrong_input(self, mock_stdout, mock_input):
        kids = get_dependent_children()
        output = mock_stdout.getvalue()
        self.assertEqual(kids, 0)
        self.assertIn("The number of kids cannot be negative. "
                      "Please enter 0 or a higher number.", output)
        self.assertIn("Invalid input: ", output)

    # Test for an applicant who is employed
    @patch("builtins.input", return_value="y")
    def test_get_employment_status_employed(self, mock_input):
        employed_applicant = get_employment_status()
        self.assertTrue(employed_applicant, True)

    # Test for an applicant who is unemployed
    @patch("builtins.input", return_value="n")
    def test_get_employment_status_unemployed(self, mock_input):
        employed_applicant = get_employment_status()
        self.assertFalse(employed_applicant, False)

    # Test for wrong input for employment status
    @patch('builtins.input', side_effect=["s", "", "-1", "  ", "0", "y"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_employment_status_wrong_input(self, mock_stdout, mock_input):
        employed = get_employment_status()
        output = mock_stdout.getvalue()
        self.assertEqual(employed, True)
        self.assertIn("No data was entered.", output)
        self.assertIn("Please enter either y or n!", output)

    # Test for income
    @patch("builtins.input", return_value=1000)
    def test_get_income(self, mock_input):
        income = get_income()
        self.assertEqual(income, 1000)

    # Test for wrong inputs for income
    @patch('builtins.input', side_effect=["s", "", "-1", "  ", "1500"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_income_wrong_input(self, mock_stdout, mock_input):
        income = get_income()
        output = mock_stdout.getvalue()
        self.assertEqual(income, 1500)
        self.assertIn("Incorrect data was entered.", output)

    # Test for expense
    @patch("builtins.input", return_value=450)
    def test_get_expenses(self, mock_input):
        expense = get_expense(1000)
        self.assertEqual(expense, 450)

    # Test for the expense if it is greater than income
    @patch("builtins.input", return_value=500)
    def test_get_expenses_greater_than_income(self, mock_input):
        expense = get_expense(400)
        self.assertEqual(expense, None)

    # Test for the expense if it is negative value or string input
    @patch("builtins.input", side_effect=["-500", "abcd", " ", "300"])
    def test_get_expenses_negative_string_input(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            expense = get_expense(500)
            output = mock_stdout.getvalue()
            self.assertEqual(expense, 300)
            self.assertIn("Expenses cannot be negative or equal to 0.", output)
            self.assertIn("Incorrect data was entered:", output)

    # Test for the loan amount
    @patch("builtins.input", return_value=5000)
    def test_get_loan_amount(self, mock_input):
        loan_amount = get_loan_amount()
        self.assertEqual(loan_amount, 5000)

    # Test for loan amount if user confirms the maximum loan amount
    @patch("builtins.input", side_effect=["25000", "y"])
    def test_loan_amount_exceeds_limit_proceed(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            loan = get_loan_amount()
            self.assertEqual(loan, 20000)

    # Test loan amount for negative inputs
    @patch("builtins.input", side_effect=["-1000", "0", "1000"])
    def test_loan_amount_negative(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            loan = get_loan_amount()
            self.assertEqual(loan, 1000)
            self.assertIn("Amount must be higher than 0.",
                          mock_stdout.getvalue())

    # Test loan amount for wrong inputs
    @patch("builtins.input", side_effect=["abc", "", " ", "1000"])
    def test_loan_for_string_inputs(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            loan = get_loan_amount()
            self.assertEqual(loan, 1000)
            self.assertIn("Incorrect data was entered:",
                          mock_stdout.getvalue())

    # Test for loan amount if user want to borrow more than 20000 and
    # cancelled the application
    @patch("builtins.input", side_effect=["25000", "no"])
    def test_loan_amount_exceeds_limit_cancel(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            loan = get_loan_amount()
            self.assertIsNone(loan)
            self.assertIn("Application cancelled!", mock_stdout.getvalue())

    # Test for monthly payment input
    @patch("builtins.input", return_value=5000)
    def test_get_motnhly_payment(self, mock_input):
        monthly_payment = get_monthly_payment(10000)
        self.assertEqual(monthly_payment, 5000)

    # Test if monthly payment > loan amount
    @patch("builtins.input", side_effect=["2000", "1000"])
    def test_monthly_payment_exceeds_loan(self, mock_input):
        loan_amount = 1000
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            get_monthly_payment(loan_amount)
            self.assertIn("The monthly payment cannot exceed the"
                          " loan amount.", mock_stdout.getvalue())

    # Test if monthly payment <= 0
    @patch("builtins.input", side_effect=["-100", "0", "100"])
    def test_negative_payment(self, mock_stdout, mock_input):
        monthly_payment = get_monthly_payment(5000)
        output = mock_stdout.getvalue()
        self.assertEqual(monthly_payment, 100)
        self.assertIn("The monthly payment must be greater than 0.", output)

    # Test if monthly payment is string
    @patch("builtins.input", side_effect=["abc", "", "100"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_negative_payment(self, mock_stdout, mock_input):
        monthly_payment = get_monthly_payment(5000)
        output = mock_stdout.getvalue()
        self.assertEqual(monthly_payment, 100)
        self.assertIn("Incorrect data was entered:", output)


if __name__ == '__main__':
    unittest.main()
