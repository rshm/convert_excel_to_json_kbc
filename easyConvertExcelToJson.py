import pandas as pd
import random
import json

# Load the Excel file
excel_file = 'easy.xlsx'

# Initialize an empty list to store the JSON objects
json_objects = []

# Counter to limit the loop to 10 iterations per sheet
counter = 0

# Read all sheets from the Excel file
all_sheets = pd.read_excel(excel_file, sheet_name=None)

# Iterate over each sheet in the Excel file
for sheet_name, df in all_sheets.items():
    print(f"Processing sheet: {sheet_name}")

    # Reset the counter for each sheet

    # Iterate over each row in the current sheet
    for index, row in df.iterrows():

        # Extract the correct answer and incorrect answers
        correct_answer = row[f'Option{row["Correct Option"]}']
        incorrect_answers = [row['OptionA'], row['OptionB'], row['OptionC'], row['OptionD']]
        incorrect_answers.remove(correct_answer)  # Remove the correct answer from the list

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

        # Increment the counter

# Save the JSON objects to a file
output_file = 'easy.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(json_objects, f, indent=4)

print(f"JSON data has been saved to {output_file}")