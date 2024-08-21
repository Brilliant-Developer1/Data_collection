import pandas as pd

def read_file(file_path):
    # Read the file into a pandas DataFrame
    return pd.read_csv(file_path, header=None)

def convert_column_to_row(df):
    # Convert the DataFrame column to a row
    return pd.DataFrame(df.values.T)

def save_to_file(df, file_path):
    # Save the DataFrame to a text file
    df.to_csv(file_path, header=False, index=False, sep='\t')

def main():
    # File paths
    input_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input file
    df = read_file(input_file)

    # Convert the column to a row
    row_df = convert_column_to_row(df)

    # Save the row to the output file
    save_to_file(row_df, output_file)

    print(f'Column data has been converted to row and saved to {output_file}')

if __name__ == "__main__":
    main()
