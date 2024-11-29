import os
import re

# Define the directory containing the PDF files
folder_path = "."

# Define the regex pattern to extract parts of the filename
#pattern = r"(.*?)((C\d+)|(T\d+)|(\d+))(.*?)\.pdf"
pattern = r"(.*?)(((T|C|H)[0-9]{5})|([0-9]{5}))(.*?)\.pdf"  #ChangeCanbeDone

paySlipString = "Payslip Apr’24" #ChangeCanbeDone
Form16String = "Form 16 FY 2023-24" #ChangeCanbeDone


# Loop through all files in the directory
for file_name in os.listdir(folder_path):
    # Process only PDF files
    if file_name.endswith(".pdf"):  #ChangeCanbeDone
        print(file_name)
        # Match the file name against the regex
        match = re.match(pattern, file_name)
        print(match.groups())
        if match:
            part1, number,part2, part3, part4, part5 = match.groups()

            # Define the new file name pattern
            #new_file_name = f"{number}_{part1.replace("(","")}.pdf"
            new_file_name = f"{number}_{Form16String}.pdf"

            # Get the full paths for renaming
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file_name} -> {new_file_name}")

print("Done!")