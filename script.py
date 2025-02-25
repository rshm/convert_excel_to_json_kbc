import pandas as pd
import random
import json

# Load the Excel file
excel_file = 'KBC.xlsx'

# Read all sheets from the Excel file
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Define output filenames for the first two sheets
output_files = ["easy.json", "difficult.json"]

# Process only the first two sheets
for idx, (sheet_name, df) in enumerate(all_sheets.items()):
    if idx >= 2:  # Only process first two sheets
        break

    print(f"Processing sheet: {sheet_name}")

    # List to store JSON objects for the current sheet
    json_objects = []

    for index, row in df.iterrows():
        # Extract the correct answer and incorrect answers
        correct_answer = row[f'Option{row["Correct Option"]}']
        incorrect_answers = [row['OptionA'], row['OptionB'], row['OptionC'], row['OptionD']]
        incorrect_answers.remove(correct_answer)  # Remove correct answer from the list

        # Randomly select one incorrect answer for the fiftyFifty option
        fifty_fifty_incorrect = random.choice(incorrect_answers)

        # Create the JSON object for the current row
        json_obj = {
            "id": row['ID'],
            "question": row['Question'],
            "answers": [
                {"text": row['OptionA'], "correct": row['Correct Option'] == 'A'},
                {"text": row['OptionB'], "correct": row['Correct Option'] == 'B'},
                {"text": row['OptionC'], "correct": row['Correct Option'] == 'C'},
                {"text": row['OptionD'], "correct": row['Correct Option'] == 'D'}
            ],
            "fiftyFifty": [correct_answer, fifty_fifty_incorrect]
        }

        # Append the JSON object to the list
        json_objects.append(json_obj)

    # Save the JSON objects to a file
    output_file = output_files[idx]
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_objects, f, indent=4)

    print(f"JSON data has been saved to {output_file}")
