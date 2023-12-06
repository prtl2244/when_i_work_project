import pandas as pd
import os

columns = ["drop", "length", "path", "user_agent", "user_id"]
combined_csv = pd.DataFrame(columns = columns)
first_run = True

# print lowercase ascii alphabet and combine csv
for x in range(97, 123): # 97 to 123
    letter = chr(x)
    csv = pd.read_csv(f"https://public.wiwdata.com/engineering-challenge/data/{letter}.csv")
    print(type(csv), letter)
    first_run = False

    if first_run == False:
        combined_csv = pd.concat([combined_csv,csv])
    
    else:
        combined_csv = csv

# Pivot csv
final_csv = combined_csv.pivot_table(index='user_id', columns='path', values='length', aggfunc='sum', fill_value=0)

# Get the directory
script_dir = os.path.dirname(os.path.abspath(__file__))
# Specify the subfolder
subfolder = 'csv_files'
# Create the subfolder path
subfolder_path = os.path.join(script_dir, subfolder)
# Create the subfolder if it doesn't exist
os.makedirs(subfolder_path, exist_ok=True)
# Save the DataFrame to a CSV file in the subfolder
csv_path = os.path.join(subfolder_path, 'final_csv.csv')
final_csv.to_csv(csv_path)

print(final_csv)