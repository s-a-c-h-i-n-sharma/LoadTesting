import os
import pandas as pd


def merge_csv_files(directory, column1, column2, output_file):
    # List all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Initialize an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)

        # Read the current CSV file
        try:
            df = pd.read_csv(file_path)
            if column1 in df.columns and column2 in df.columns:
                df = df[[column1, column2]]
                # Append the data to the merged DataFrame
                merged_data = merged_data._append(df, ignore_index=True)
            else:
                print(f"Columns '{column1}' or '{column2}' not found in file: {csv_file}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Save the merged data to the output CSV file
    merged_data.to_csv(output_file, index=False)


# Example usage
directory = r'D:\Magicbox-loadtesting\CSVs\updated\teacherslist'
column1 = 'Username'
column2 = 'User_guid'
output_file = r'D:\Magicbox-loadtesting\CSVs\updated\teacherslist\merged_10k_username_and_user_guid.csv'

merge_csv_files(directory, column1, column2, output_file)