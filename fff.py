import pandas as pd
import json

# Load the Excel file
excel_file = 'fff.xlsx'  # Replace with your Excel file path
df = pd.read_excel(excel_file)

# Print the column names to debug
print("Columns in the Excel file:", df.columns.tolist())

# Initialize an empty list to store the JSON objects
json_objects = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Create the JSON object for the current row
    json_obj = {
        "id": row['ID'],  # Ensure this matches the column name in your Excel file
        "question": row['Question'],  # Ensure this matches the column name in your Excel file
        "answers": [
            {"text": f"A. {row['OpetionA']}"},  # Prefix with "A."
            {"text": f"B. {row['OptionB']}"},  # Prefix with "B."
            {"text": f"C. {row['OptionC']}"},  # Prefix with "C."
            {"text": f"D. {row['OptionD']}"}  # Prefix with "D."
        ],
        "correctAnswer": row['Correct Answer'].lower()  # Ensure this matches the column name in your Excel file
    }

    # Append the JSON object to the list
    json_objects.append(json_obj)

# Convert the list of JSON objects to a JSON string
json_str = json.dumps(json_objects, indent=4)

# Save the JSON string to a file
output_file = 'fff.json'
with open(output_file, 'w') as f:
    f.write(json_str)

print(f"JSON data has been saved to {output_file}")