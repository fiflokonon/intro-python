def read_and_modify_file(input_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
            # Example modification: convert content to uppercase
            modified_content = content.upper()
            return modified_content
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except IOError:
        print("Error: Unable to read the file.")
        return None

def write_to_new_file(output_filename, content):
    try:
        with open(output_filename, 'w') as file:
            file.write(content)
            print(f"Modified content successfully written to '{output_filename}'.")
    except IOError:
        print("Error: Unable to write to the file.")

def main():
    input_filename = input("Enter the name of the file to read: ").strip()
    modified_content = read_and_modify_file(input_filename)

    if modified_content is not None:
        output_filename = input("Enter the name of the new file to save modified content: ").strip()
        write_to_new_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
