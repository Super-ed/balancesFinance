# Read data from the file 
with open("1st.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Prepare a list to hold the processed account codes
processed_codes = []

# Process each line
for line in lines:
    # Split the line into code and name
    code, name = line.split(maxsplit=1)

    # Pad the code to 9 digits with zeros
    padded_code = code.ljust(9, '0')

    # Insert dots every 3 digits
    formatted_code = '.'.join([padded_code[i:i+3] for i in range(0, len(padded_code), 3)])

    # Add the formatted code and name to the list
    processed_codes.append(formatted_code + ' ' + name)

# Write the processed account codes to a new text file
with open('planDeCuentas.txt', 'w') as file:
    file.writelines(processed_codes)

# python AccountsAutopilot.py