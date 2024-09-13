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

### Remaining Bugs

### Validator Testing

## Deployment