# Read data from the file 
with open("Balance.txt", "r") as file:
    lines = file.readlines()

# Split the data into sections based on the blank lines 
    sections = [section.strip().split('\n') for section in ''.join(lines).split('\n\n')]

# Extract headers and values for each section
    headers = sections[0]
    values = sections[1:]

# Remove the date labels
    headers = headers[1:]
    values = [value[1:] for value in values]


# Replace "-" with 0
    values = [[entry.replace('-', '0') for entry in value] for value in values]


# Transpose the values matrix
    values_transposed = list(map(list, zip(*values)))

# Write the data to a new text file
with open('output.txt', 'w') as file:
    # Write headers
    file.write('\t'.join(headers) + '\n')
    # Write values
    for i, row in enumerate(values_transposed):
        if i % 2 == 0:
            file.write('\t'.join(row) + '\n')
    
