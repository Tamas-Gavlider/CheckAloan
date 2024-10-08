# CheckAloan

Checkaloan is a Python terminal-based application that evaluates the loan eligibility of a user.<br>
The name of the app rhymes with "Check Alone" because users typically check their loan eligibility on their own. That's why the app greets them with the message "Where you are not alone" to reassure them that CheckAloan is here to help. The app calculates a score and interest rate based on the user's input and provides a final decision on the loan approval.<br> The app runs on Heroku.

[Here is the live version of my project](https://checkaloan-cdfe97fe02ce.herokuapp.com/)

![AmIResponsive](docs/screenshots/am-i-responsive.png)

## Contents
- [How to Use](#how-to-use)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Data Model](#data-model)
  - [Excel](#excel)
  - [Flowchart](#flowchart)
  - [Data Handling](#data-handling)
    - [Constant and global variables](#constant-and-global-variables)
    - [Outside Functions](#outside-functions)
    - [Applicant Class](#applicant-class)
  - [Libraries](#libraries)
- [Testing](#testing)
  - [Bugs](#bugs)
  - [Remaining Bugs](#remaining-bugs)
  - [Validator Testing](#validator-testing)
  - [Unit Testing](#unit-testing)
- [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## How to Use

- The user provides personal and financial details such as income, expenses, age, marital status, etc.
- The app calculates the score and interest rate based on this information.
- Based on the calculated score, the app makes a final decision:
    - <bold>Approved</bold> if the user is eligible for the loan.
    - <bold>Rejected</bold> if the user is not eligible.

## Features

### Existing Features

 - Option to start the application form or quit the app.
 - Accepts user inputs.
 - Add the user's data to the database after the final decision
 - Input validation and error-checking
    - The user must press 1 to start the application or press 2 to close it.<br> Other characters or no input will not be accepted.<br>
    ![Welcome screen](/docs/gif/welcome-page.gif)
    ![Start app](/docs/gif/start-app.gif)
    - String inputs like name and phone must meet minimum/maximum length requirements.<br>
      - Name validation<br>![Name-GIF](/docs/gif/name-validation.gif)
      - Phone number validation<br>![Phone-GIF](/docs/gif/phone-validation.gif)
      - Marital status validation<br>![Marital-status-GIF](/docs/gif/marital-status-validation.gif)
    - A robust email validation method was used for email input.<br>![Email-GIF](/docs/gif/email-validation.gif)
    - Integer inputs will raise an error if 0, a string or no data is entered.
        - Number of dependent children<br>![Number-of-kids-GIF](/docs/gif/validation-dependent-children.gif)
        - Income and Expense validation. Application will be cancelled if expense exceeds the income.<br>
        ![Income-expense](/docs/gif/income-validation.gif)<br>
        ![Income-expense](/docs/gif/expense-validation.gif)
    - If the input for age is less than 18 or more than 65, the loan application will be canceled,<br> and the user will be taken back to the welcome page.
        - Age with wrong inputs<br>![Age-gif](/docs/gif/age-validation.gif)
        - Age under 18<br>![Age-under-18](/docs/screenshots/age-under-18.png)
        - Age over 65<br>![Age-over-65](/docs/screenshots/age-over-65.png)
        - Age between 18 - 65<br>![Age-valid](/docs/gif/age-validation-valid-age.gif)
    - If the user is unemployed the application will be cancelled,
    <br>and the user will be taken back to the welcome page.<br>
    ![Employment](/docs/gif/employment-validation-unemployed.gif)
    - The loan amount cannot exceed 20,000. If a higher amount is entered, the user will be notified<br> and can choose to proceed with the maximum amount or cancel the application.<br>
    ![Loan amount](/docs/gif/loan-amount-validation.gif)
    - The monthly payment cannot exceed the loan amount. The user will be asked to adjust<br> the monthly payment.<br>
    ![Monthly payment](/docs/gif/monthly-payment-validation.gif)
    - The monthly payment should be calculated to ensure the loan is repaid in no more than 60 months.<br>
    ![Error message](/docs/screenshots/monthly-payment-error-for-low-amount.png)
    - The application will be cancelled if the expense is greater than the income.
    <br>![Expense>Income](/docs/screenshots/expense-greater-than-income.png)

### Future Features

User will have an option to schedule an appointment with a financial advisor after the submission of the application.<br>
Additional inputs from the customer, such as any missed payments in the past or a criminal record<br>
The user will also have an option to choose the monthly payment and loan term rather than the loan amount.

## Data Model

### Excel 

The main features, scoring system, interest rate calculation, and criteria were initially created in an [Excel sheet](/docs/roadmap.xlsx).

### Flowchart
To help visualize the structure and logic of the code, I have created a flowchart that outlines the main components and their interactions.
![flowchart](docs/flowchart.png)

### Data Handling

Data maintaned in class instances. Some functions are handled outside of the class for simplicity and testing purposes.<br> 

#### Constant and Global variables

- **database** is an empty dictionary to store the user details.
- **MIN SCORE** 70 points that needs to be reached for approval.
- **MAX LOAN** the maximum loan amount of 20 000.
- **MAX LOAN DURATION** - Max loan repayment length in months.
- **application ID** - will serve as the key in the database.

#### Outside Functions
- **standard_style** add color and style. The color is set to green and style to bright for better visibility.
- **wrong_input** will change the text color to red if the input is invalid or the application is rejected.
- **welcome_message** will greet the user and, based on the input, either start the application or close it.
- **get_functions** will validate and return the user inputs.
- **applicant_details** will return the user inputs, which will be used to create a class object.
- **run** this function will manage the execution of the application.

#### Applicant Class

- **summary** - will return the user details.<br>
- **change functions** - change the user details. These functions are using the same validation methods as the get functions outside the class. Exceptions are:
  - **change employment** - if the user will change the employment status, it will not auto cancel the application. Instead -120 points will be added to the score so the minimum score cannot be reached. This will guarantee the rejection. The reason I kept it this way is that the user might change this detail by mistake, and it would not provide a good user experience if the entire form had to be filled out again.<br>
  ![Change employment](/docs/gif/change-employment.gif)
  - **change income** - had to make sure the input will not be accepted if the user press enter without providing any inputs. It would let the user to enter negative amount or lower amount than the expense.<br>
  ![Change income](/docs/gif/change-income.gif)
  - **change loan** - I wanted to make sure that the monthly payment will fit within the 60-month term. If the loan amount changes, the monthly payment will be automatically recalculated to stay within this term.<br>
  ![Change loan](/docs/gif/change-loan.gif)
- **make changes** - user will need to press n to make changes or press enter to submit the form. Validation done to make sure that other input will not be accepted.<br>
![Make changes](/docs/gif/make-changes.gif)
- **check duplicates** - will check if the user had any prior application with us. It will search for the email address. Function will return the previous application status with the loan details if duplicate found. Otherwise it will calculate the score and interest rate.
![Duplicate](/docs/screenshots/duplicate-message.png)
- **calculate functions** - once the details are confirmed , for each detail the score and interest rate will be calculated. 
- **status function** - will return either "APPROVED" or "REJECTED".
- **decision function** - will return the loan details and monthly payment with interest rate for the approved application or the rejection message with the score.<br>
![Approved](/docs/screenshots/decision.png)<br>
![Rejected](/docs/screenshots/rejected.png)
- **add to database** - any applications get by the decision phase will be added to the database regardless the outcome. Beside the name and email address no other personal details will be stored. This function will increment the **application ID** by one to make sure the applications will not be replaced in the database.

### Libraries

The following libraries were used:
- Colorama to add color to the text. The text is set to green by default. It changes to red for wrong input or if the application is rejected, and to blue if the user submits a duplicate request.
- Tabulate to display the user details in a table.<br>
![Summary](/docs/screenshots/summary-ss.png)
- RegEx used for name, phone and email validation

## Testing

### Bugs

There was a logical error in the make_changes function, which allowed the loan amount to be set higher than 20,000. A while True loop was implemented to prevent this issue by continuously prompting the user to enter a lower amount. A similar bug occurred with the monthly payment, where users were able to set the monthly payment higher than the total loan amount. This was also resolved using a while True loop, ensuring that the monthly payment cannot exceed the loan amount and that the loan term does not exceed sixty months.

### Remaining Bugs

No bugs remaining.

### Validator Testing

- PEP8 
    - No errors were returned from [PEP8](https://pep8ci.herokuapp.com/)
     Unit test<br>![Pep8unittest](/docs/validation/unittest-pep8.png)<br>
     Run file<br>![Run.py](/docs/validation/run-file-pep8.png)<br>


### Unit Testing

Unit testing returned no errors.

![Unittest](/docs/validation/unittest.png)

## Deployment

This project was deployed used Code Institute's mock terminal for [Heroku](https://dashboard.heroku.com/apps).<br>
Steps for deployment:
- Fork or clone the repository CheckAloan
- Create a new Heroku app 
- Set the buildbacks for **Python** and **NodeJS** in that order
- You must then create a Config Var called PORT. Set this to 8000.
- Link the Heroku app to the repository
- Click on <strong>Deploy</strong>

### Local Development

#### How to Fork

To fork the CheckAloan repository:
  - Log in (or sign up) to Github.
  -  Go to the repository for this project, Tamas-Gavlider/CheckAloan.
  - Click the Fork button in the top right corner.

#### How to Clone

To clone the CheckAloan repository:

- Log in (or sign up) to Github.
- Go to the repository for this project, Tamas-Gavlider/CheckAloan.
- Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Credits 

Code Institute for the deployment terminal and Readme template.

For unit testing, I utilized methods and examples from the following resources:
  - [andressa.dev](https://andressa.dev/2019-07-20-using-pach-to-test-inputs/) 
  - [sophieau.com](https://sophieau.com/article/python-in-out-err-mocking/)<br>
  - [python.org](https://docs.python.org/3/library/unittest.mock.html)<br>

These resources provided valuable insights into testing input handling and mocking techniques.

For email validation, I referenced the following resource to implement more complex checks beyond just "@" and ".":
- [Javatpoint](https://www.javatpoint.com/how-to-validated-email-address-in-python-with-regular-expression.)
This resource helped in applying regular expressions for robust email validation.

For name and phone validation, I referenced to the following resource:
- [W3chools](https://www.w3schools.com/python/python_regex.asp#gsc.tab=0)

### Acknowledgements

I would like to acknowledge my Code Institute mentor Graeme Taylor for his valuable advices.