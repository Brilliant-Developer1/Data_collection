def generate_numbers():
    # Generate the sequence 1 to 13, 260 times
    numbers = []
    for _ in range(260):
        numbers.extend(range(1, 14))
    return numbers

def save_to_file(data, file_path):
    # Save the data to a text file
    with open(file_path, 'w') as file:
        for number in data:
            file.write(f"{number}\n")

def main():
    # File path
    output_file = '/Users/abidhassan/Documents/Code/Python/Data_collection/GlobeMusic/output.txt'

    # Generate the numbers
    numbers = generate_numbers()

    # Save the numbers to the output file
    save_to_file(numbers, output_file)

    print(f'The numbers have been written to {output_file}')

if __name__ == "__main__":
    main()
