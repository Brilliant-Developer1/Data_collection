import os

def load_mapping(mapping_file):
    mapping = {}
    with open(mapping_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                new_name, old_name = parts
                mapping[old_name] = new_name
    return mapping

def rename_images(folder_path, mapping):
    for old_name, new_name in mapping.items():
        old_file_path = os.path.join(folder_path, f"{old_name}")
        if os.path.exists(old_file_path):
            file_extension = os.path.splitext(old_file_path)[1]
            new_file_path = os.path.join(folder_path, f"{new_name}{file_extension}")
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{old_file_path}' to '{new_file_path}'")
        else:
            print(f"File '{old_file_path}' not found.")

if __name__ == "__main__":
    # Specify the path to the folder containing the images
    folder_path = './images'  # Change this to your folder path
    # Specify the path to the mapping file
    mapping_file = 'mapping.txt'  # Change this to your mapping file path

    mapping = load_mapping(mapping_file)
    rename_images(folder_path, mapping)
