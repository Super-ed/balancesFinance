# Read data from the file 
with open("Balance.txt", "r") as file:
    lines = file.readlines()

# Find the start and end of the account names section
start = lines.index("Accounts\n") + 1
end = lines.index("Accounts\n", start)

# Extract the account names
account_names = [line.strip() for line in lines[start:end]]

# Find the start of the balances section
start_balances = lines.index("Jun-21\n") + 1
end_balances = lines.index("Jun-22\n")

# Extract the balances
balances_jun_21 = [line.strip().replace('-', '0') for line in lines[start_balances:end_balances]]

# Find the start of the balances section for Jun-22
start_balances = lines.index("Jun-22\n") + 1
end_balances = lines.index("Jun-23\n")

# Extract the balances for Jun-22
balances_jun_22 = [line.strip().replace('-', '0') for line in lines[start_balances:end_balances]]

# Find the start of the balances section for Jun-23
start_balances = lines.index("Jun-23\n") + 1
end_balances = lines.index("Sep-23\n")

# Extract the balances for Jun-23
balances_jun_23 = [line.strip().replace('-', '0') for line in lines[start_balances:end_balances]]

# Find the start of the balances section for Sep-23
start_balances = lines.index("Sep-23\n") + 1
end_balances = len(lines)

# Extract the balances for Sep-23
balances_sep_23 = [line.strip().replace('-', '0') for line in lines[start_balances:end_balances]]

# Pair the account names with their balances
account_balances = list(zip(account_names, balances_jun_21, balances_jun_22, balances_jun_23, balances_sep_23))

# Write the account names and balances to a new text file
with open('AccountBalances.txt', 'w') as file:
    for name, balance_21, balance_22, balance_23, balance_sep in account_balances:
        file.write(name + ' | ' + balance_21 + ' | ' + balance_22 + ' | ' + balance_23 + ' | ' + balance_sep + '\n')
# python OrganizerAutopilot.py