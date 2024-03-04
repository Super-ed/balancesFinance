# Read data from the file 
with open("AccountBalances.txt", "r") as file:
    lines = file.readlines()

# Prepare a dictionary to hold the account codes
account_codes = {}

# Read data from the planDeCuentas.txt file
with open("planDeCuentas.txt", "r") as file:
    for line in file:
        # Split the line into code and name
        code, name = line.split(maxsplit=1)

        # Remove newline character from name and convert to uppercase
        name = name.strip().upper()

        # Add the code and name to the dictionary
        account_codes[name] = code

# Prepare a list to hold the processed account balances
processed_balances = []

# Process each line
for line in lines:
    # Split the line into name and balances
    name, balances = line.split(' | ', maxsplit=1)

    # Convert name to uppercase
    name_upper = name.upper()

    # Get the code for the account name
    code = account_codes.get(name_upper, 'Unknown')

    # Add the code, original name, and balances to the list
    processed_balances.append(code + ' ' + name + ' | ' + balances)

# Write the processed account balances to a new text file
with open('AccountBalancesWithCodes.txt', 'w') as file:
    file.writelines(processed_balances)
# python AccountsCodesAndSaldos.py