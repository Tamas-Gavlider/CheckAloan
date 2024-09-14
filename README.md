# CheckAloan

Checkaloan is aPython terminal-based application that evaluates the loan eligibility of a user.<br> The app calculates a score and interest rate based on the user's input and provides a final decision on the loan approval.<br> The app runs on Heroku.

## How to use

- The user provides personal and financial details such as income, expenses, age, marital status, etc.
- The app calculates the score and interest rate based on the provided information.
- Based on the calculated score, the app makes a final decision:
    - Approved if the user is eligible for the loan.
    - Rejected if the user is not eligible.

## Features

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

### Future Features

## Data Model

## Testing

### Bugs

There was a logical error in the make_changes function, which allowed the loan amount to be set higher than 20,000. A while True loop was implemented to prevent this issue by continuously prompting the user to enter a lower amount. A similar bug occurred with the monthly payment, where users were able to set the monthly payment higher than the total loan amount. This was also resolved using a while True loop, ensuring that the monthly payment cannot exceed the loan amount and that the loan term does not exceed sixty months.

### Remaining Bugs

### Validator Testing

## Deployment

App deployed via [Heroku](https://dashboard.heroku.com/apps).