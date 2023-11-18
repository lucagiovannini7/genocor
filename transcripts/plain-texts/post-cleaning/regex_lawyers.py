import re

with open('/Users/miriam/Documents/GitHub/genocor/transcripts/plain-texts/post-cleaning/RWA-Muhimana-full.txt', 'r') as file:
    lines = file.readlines()

new_lines = []

ignore_line = False  # Flag to ignore lines

for line in lines:
    
    line = line.replace("@THE ACCUSED MUHIMANA:", "@MIKA MUHIMANA:")

    if line.startswith('$By order of the Court'):
        ignore_line = True
    elif line.startswith('$BY '):
        # Extract characters after "$BY "
        extracted_text = line[len('$BY '):].strip()
        # Append the $BY line without replacement
        new_lines.append(line)
        ignore_line = False  # Reset the flag when a new "$BY" line is encountered
    elif line.startswith('@Q.') and 'extracted_text' in locals() and not ignore_line:
        # Replace lines starting with "@Q." with extracted text
        new_lines.append("@" + extracted_text + '\n')
    elif not ignore_line:
        # Append the line if it doesn't match the conditions to ignore or replace
        new_lines.append(line)




# Write the modified content to a new file
with open('output_lawyers.txt', 'w') as file:
    file.writelines(new_lines)