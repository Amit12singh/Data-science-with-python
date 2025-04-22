import pdb

from grade import calculate_grade, is_passing


def process_student_data(input_file, output_file, attendance=85):
    results = []

    try:
        with open(input_file, 'r') as file:
            for line_number, line in enumerate(file, 1):
                print(f"Processing line {line_number}: {line.strip()}")
                try:
                    pdb.set_trace()  # Start debugging here
                    name, score = line.strip().split(',')
                    score = float(score)
                    if not (0 <= score <= 100):
                        print(f"Invalid score {score}. Skipping.")
                        continue
                    grade = calculate_grade(score)
                    passing = is_passing(score, attendance)
                    results.append((name, score, grade, "Pass" if passing else "Fail"))
                except ValueError as e:
                    print(f"Line {line_number}: ValueError - {e}")
        with open(output_file, 'w') as file:
            file.write("Name,Score,Grade,Status\n")
            for name, score, grade, status in results:
                file.write(f"{name},{score:.1f},{grade},{status}\n")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")