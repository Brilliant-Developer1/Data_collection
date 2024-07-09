import pandas as pd


def read_file(file_path):
    # Read the file into a pandas DataFrame
    return pd.read_csv(file_path, sep='\t')


def update_artists(df_list1, df_list2):
    # Find rows in List 1 where Spotify Artist ID and Apple Music ID are missing
    missing_ids = df_list1[(df_list1["Spotify Artist ID"] == 'request') | (
        df_list1["Apple Music ID"] == 'request')]

    # Update the missing IDs from List 2
    for index, row in missing_ids.iterrows():
        artist_name = row["Artist Name"]
        match = df_list2[df_list2["Artist Name"] == artist_name]
        if not match.empty:
            if row["Spotify Artist ID"] == 'request':
                df_list1.at[index,
                            "Spotify Artist ID"] = match.iloc[0]["Spotify Artist ID"]
            if row["Apple Music ID"] == 'request':
                df_list1.at[index,
                            "Apple Music ID"] = match.iloc[0]["Apple Music ID"]

    return df_list1


def save_to_file(df, file_path):
    # Save the DataFrame to a text file
    df.to_csv(file_path, sep='\t', index=False)


def main():
    # File paths
    file_list1 = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input.txt'
    file_list2 = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/input2.txt'
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Read the input files
    df_list1 = read_file(file_list1)
    df_list2 = read_file(file_list2)

    # Update artists in List 1 with information from List 2
    updated_list = update_artists(df_list1, df_list2)

    # Save the updated list to the output file
    save_to_file(updated_list, output_file)

    print(f'Updated artist list has been saved to {output_file}')


if __name__ == "__main__":
    main()
