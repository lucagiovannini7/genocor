import re


with open('/Users/miriam/Documents/GitHub/genocor/output_lawyers.txt', 'r') as file:
    lines = file.readlines()
    
new_lines = []

ignore_line = False  # Flag to ignore lines

for line in lines:
    
    if line.startswith('$Declaration made by'):
        # Extract characters after "$BY "
            words_after_by = line.split("by")[1].strip().split()[:2]
            capitalized_words = [word.upper() for word in words_after_by]
            extracted_text = "@" + " ".join(capitalized_words) + ":"
        # Append the $BY line without replacement
            new_lines.append(line)
            ignore_line = False  # Reset the flag when a new "$BY" line is encountered
            print("Extracted Text:", extracted_text)  # Print the extracted text name

    elif line.startswith('@A.') and 'extracted_text' in locals() and not ignore_line:
        # Replace lines starting with "@Q." with extracted text
        new_lines.append(extracted_text + '\n')
    elif line.startswith('@THE WITNESS:') and 'extracted_text' in locals() and not ignore_line:
        # Replace lines starting with "@Q." with extracted text
        new_lines.append(extracted_text + '\n')
    elif not ignore_line:
        # Append the line if it doesn't match the conditions to ignore or replace
        new_lines.append(line) 

for i, line in enumerate(new_lines):
    if '@LIVINUS CHO:' in line:
        new_lines[i] = line.replace("@LIVINUS CHO:", "@MR. LIVINUS CHO ATANGA:")
    elif '@THE WITNESS,:' in line:
        new_lines[i] = line.replace("@THE WITNESS,:", "@MR. ANTONIUS MARIA LUCASSEN")
    elif '@THE WITNESS:' in line:
        new_lines[i] = line.replace("@THE WITNESS:", "@WITNESS DG:")

    
# Write the modified content to a new file
with open('output_witnesses.txt', 'w') as file:
    file.writelines(new_lines)