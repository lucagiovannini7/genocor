# Find duplicate transcripts

file_path = '/Users/miriam/Documents/GitHub/genocor/transcripts/plain-texts/post-cleaning/regex-lawyers-Muhimana.py'  

def find_duplicate_sequences(file_path, sequence_length=20):
    current_sequence = []
    duplicate_sequences = []
    line_number = 0

    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            line = line.strip()
            if current_sequence and line != current_sequence[-1]:
                if len(current_sequence) >= sequence_length:
                    duplicate_sequences.append((current_sequence[0], line_number - len(current_sequence) + 1))
                current_sequence = []
            current_sequence.append(line)
            line_number = line_num

    if current_sequence and len(current_sequence) >= sequence_length:
        duplicate_sequences.append((current_sequence[0], line_number - len(current_sequence) + 1))

    if not duplicate_sequences:
        print(f"No duplicate sequences of {sequence_length} or more lines found.")
    else:
        print(f"Duplicate sequences of {sequence_length} or more lines found:")
        for sequence, start_line in duplicate_sequences:
            print(f"Sequence '{sequence}' first appears at line number: {start_line}")


find_duplicate_sequences(file_path)
