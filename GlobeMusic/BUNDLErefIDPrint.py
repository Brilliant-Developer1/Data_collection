# Function to save codes to a file 88 times each
def save_codes_to_file(filename):
    start_code = 281
    end_code = 395

    with open(filename, 'w') as file:
        for code in range(start_code, end_code + 1):
            code_str = f'C0{code}'
            for _ in range(10):
                file.write(code_str + '\n')


# Call the function and save the output to output.txt
save_codes_to_file('output.txt')
