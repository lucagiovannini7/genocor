import os
import re

def extract_dates_with_capitalized_words(text):
    date_pattern = re.compile(r'\b(?:\d{1,2} [A-Z]+ \d{4}|(?:[A-Z]+DAY, )?\d{1,2} [A-Z]+ \d{4})\b')
    dates = date_pattern.findall(text)

    # Delete everything before the first number in each date
    dates = [re.sub(r'^.*?(\d{1,2} [A-Z]+ \d{4})', r'\1', date) for date in dates]

    return dates

def process_files(folder_path, excluded_files, output_file):
    with open(output_file, 'w') as output:
        txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt') and file not in excluded_files]

        for txt_file in txt_files:
            file_path = os.path.join(folder_path, txt_file)

            with open(file_path, 'r') as file:
                text = file.read()

            extracted_dates = extract_dates_with_capitalized_words(text)

            if extracted_dates:
                output.write(f"\nFile: {txt_file}\n")
                output.write(f"Number of transcripts extracted: {len(extracted_dates)}\n")
                for date in extracted_dates:
                    output.write(date + '\n')
            else:
                output.write(f"\nFile: {txt_file}\n")
                output.write("No dates with capitalized words found.\n")

def list_txt_files_exclude_specific(folder_path, excluded_files):
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt') and file not in excluded_files]
    return txt_files

folder_path = '/Users/miriam/Documents/GitHub/genocor/transcripts/plain-texts/post-cleaning'
excluded_files = ['RWA-Muhimana-full.txt', 'RWA-Ndindabahizi-full.txt', 'overview-extracted-transcripts-by-date.txt']
output_file = '/Users/miriam/Documents/GitHub/genocor/transcripts/plain-texts/post-cleaning/overview-extracted-transcripts-by-date.txt'

txt_files = list_txt_files_exclude_specific(folder_path, excluded_files)

if txt_files:
    # Process the files and extract dates with capitalized words, then save results to a file
    process_files(folder_path, excluded_files, output_file)
    print(f"Results saved to {output_file}")
else:
    print("No .txt files found in the 'post-cleaning' folder (excluding specific files).")
