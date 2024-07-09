import pandas as pd


def read_file(file_path):
    # Read the file into a pandas DataFrame
    return pd.read_csv(file_path, sep='\t')


def compare_lists(df_list1, df_list2):
    # Identify new artists in List 2 that are not present in List 1
    new_artists = df_list2[~df_list2["Artist Name"].isin(
        df_list1["Artist Name"])]
    return new_artists


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

    # Compare the lists and find new artists
    new_artists = compare_lists(df_list1, df_list2)

    # Save the new artists to the output file
    save_to_file(new_artists, output_file)

    print(f'New artists have been saved to {output_file}')


if __name__ == "__main__":
    main()
