import os
import re
from collections import defaultdict

def rename_sequences(directory):
    # Regular expression to extract prefix and sequence number
    sequence_pattern = re.compile(r"([a-zA-Z0-9_-]+)_(\d{2})\.(jpg|png|jpeg)$")
    
    # Store files grouped by name and extension
    sequences = defaultdict(list)
    
    # Step 1: Group images by sequence name and extension
    for filename in os.listdir(directory):
        match = sequence_pattern.match(filename)
        if match:
            prefix, seq_num, extension = match.groups()
            sequences[(prefix, extension)].append((seq_num, filename))
    
    # Step 2: Rename files within each sequence
    for (prefix, extension), files in sequences.items():
        # Sort files by the sequence number
        files.sort(key=lambda x: x[0])
        
        # Rename files sequentially
        for index, (old_num, old_filename) in enumerate(files):
            # New filename with padded number (01, 02, ..., N)
            new_num = f"{index + 1:02d}"
            new_filename = f"{prefix}_{new_num}.{extension}"
            old_filepath = os.path.join(directory, old_filename)
            new_filepath = os.path.join(directory, new_filename)
            
            print(f"Renaming {old_filename} -> {new_filename}")
            os.rename(old_filepath, new_filepath)
            
    print("Renaming complete.")

# Example usage
if __name__ == "__main__":
    directory = input("Enter the path to the directory containing the images: ")
    rename_sequences(directory)

