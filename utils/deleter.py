import os

def delete_every_second_line(file_path):
    with open(file_path, 'rb') as file:
        lines = file.readlines()

    # Decode each line to string
    lines = [line.decode('utf-8', errors='ignore') for line in lines]

    # Remove every second line
    new_lines = [line for index, line in enumerate(lines) if index % 2 == 0]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

if __name__ == "__main__":
    file_name = "rockyou.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    if os.path.exists(file_path):
        delete_every_second_line(file_path)
        print(f"Every second line in {file_name} has been deleted.")
    else:
        print(f"The file {file_name} does not exist in the same directory as the script.")
