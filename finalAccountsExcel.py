# import openpyxl
# import time

# # Create a new workbook and select the active sheet
# wb = openpyxl.Workbook()
# sheet = wb.active

# # Set the headers in the first row
# headers = ['Código', 'Cuenta', 'jun-21', 'jun-22', 'jun-23', 'sep-23']
# sheet.append(headers)

# # Read data from the file 
# with open("AccountBalancesWithCodes.txt", "r") as file:
#     lines = file.readlines()

# # Process each line
# for line in lines:
#     # Insert ' | ' between the account code and the account name
#     line = line.replace(' ', ' | ', 1)

#     # Split the line into parts
#     parts = line.split(' | ')

#     # Skip lines that do not have the correct number of parts
#     if len(parts) != 6:
#         continue

#     # Unpack the parts into variables
#     code, name, jun_21, jun_22, jun_23, sep_23 = parts

#     # Remove periods from the balances and convert them to integers
#     jun_21 = int(jun_21.replace('.', ''))
#     jun_22 = int(jun_22.replace('.', ''))
#     jun_23 = int(jun_23.replace('.', ''))
#     sep_23 = int(sep_23.replace('.', ''))

#     # Add the data to the sheet
#     sheet.append([code, name, jun_21, jun_22, jun_23, sep_23])

#     # Print the line and pause for 0.3 seconds
#     print(f"Processing line: {line}")
#     time.sleep(0.3)

# # Save the workbook to an Excel file
# wb.save('AccountBalancesWithCodes1.xlsx')

import openpyxl
import time

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Set the headers in the first row
headers = ['Código', 'Cuenta', 'Fecha', 'Saldo']
sheet.append(headers)

# Read data from the file 
with open("AccountBalancesWithCodes.txt", "r") as file:
    lines = file.readlines()

# Process each line
for line in lines:
    # Insert ' | ' between the account code and the account name
    line = line.replace(' ', ' | ', 1)

    # Split the line into parts
    parts = line.split(' | ')

    # Skip lines that do not have the correct number of parts
    if len(parts) != 6:
        continue

    # Unpack the parts into variables
    code, name, jun_21, jun_22, jun_23, sep_23 = parts

    # Remove periods from the balances and convert them to integers
    jun_21 = int(jun_21.replace('.', ''))
    jun_22 = int(jun_22.replace('.', ''))
    jun_23 = int(jun_23.replace('.', ''))
    sep_23 = int(sep_23.replace('.', ''))

    # Add the data to the sheet, one row for each date
    sheet.append([code, name, 'jun-21', jun_21])
    sheet.append([code, name, 'jun-22', jun_22])
    sheet.append([code, name, 'jun-23', jun_23])
    sheet.append([code, name, 'sep-23', sep_23])

    # Print the line and pause for 0.3 seconds
    print(f"Processing line: {line}")
    time.sleep(0.3)

# Save the workbook to an Excel file
wb.save('AccountBalancesWithCodes3.xlsx')

# python finalAccountsExcel.py