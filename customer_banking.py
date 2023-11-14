# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please enter the savings account balance: "))
    savings_interest = float(input("Please enter the savings account interest rate: "))
    savings_maturity = int(input("Please enter the savings account interest period (months): "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nSavings Account Balance is: ${updated_savings_balance:,.2f}")
    print(f"\nSavings Account Interest Earned over {savings_maturity} months is: ${interest_earned:,.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Please enter the CD account balance: "))
    cd_interest = float(input("Please enter the CD account interest rate: "))
    cd_maturity = int(input("Please enter the CD account interest period (months): "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nCD Account Balance is: ${updated_cd_balance:,.2f}")
    print(f"\nCD Account Interest Earned over {cd_maturity} months is: ${interest_earned:,.2f}\n")

if __name__ == "__main__":
    # Call the main function.
    main()
