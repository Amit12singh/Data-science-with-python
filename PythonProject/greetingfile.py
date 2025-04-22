def read_names_from_file(input_file):
    try:
        with open(input_file, 'r') as file:
            names = [line.strip() for line in file if line.strip()]
        return names
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return []

def write_greetings_to_file(names, output_file):
    with open(output_file, 'w') as file:
        for name in names:
            greeting = f"Hello {name}! Hope you're having an awesome day!\n"
            file.write(greeting)
    print(f"✅ Greetings written to '{output_file}' successfully.")

def main():
    input_filename = "names.txt"
    output_filename = "greetings.txt"

    names = read_names_from_file(input_filename)
    if names:
        write_greetings_to_file(names, output_filename)

if __name__ == "__main__":
    main()
