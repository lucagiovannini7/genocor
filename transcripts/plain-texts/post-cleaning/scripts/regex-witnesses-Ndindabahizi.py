import re


with open('/Users/miriam/Documents/GitHub/genocor/transcripts/plain-texts/post-cleaning/RWA-Ndindabahizi-output-lawyers.txt', 'r') as file:
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
    if '@WITNESS UPENDRA:' in line:
        new_lines[i] = line.replace("@WITNESS UPENDRA:", "@MR. UPENDRA SINGH BAGHEL:")
    elif '@ALISON DES:' in line:
        new_lines[i] = line.replace("@ALISON DES:", "@MS. ALISON DES FORGES:")
    elif '@BERNARD LUGAN:' in line:
        new_lines[i] = line.replace("@BERNARD LUGAN:", "@MR. BERNARD LUGAN:")
    elif '@EMMANUEL NDINDABAHIZI:' in line:
        new_lines[i] = line.replace("@EMMANUEL NDINDABAHIZI:", "@MR. EMMANUEL NDINDABAHIZI:")
    
# Write the modified content to a new file
with open('/Users/miriam/Documents/GitHub/genocor/transcripts/plain-texts/post-cleaning/RWA-Ndindabahizi-output-witnesses.txt', 'w') as file:
    file.writelines(new_lines)