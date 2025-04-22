def calculate_grade(score):
    """Convert numeric score to letter grade."""
    print(f"Calculating grade for score: {score}")  # Debug: Show input score
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 0:
        return "F"
    else:
        return None


def is_passing(score, attendance):
    """Determine pass/fail status."""
    print(f"Checking pass/fail: score={score}, attendance={attendance}")  # Debug
    return score >= 70 and attendance >= 80


def process_student_data(input_file, output_file, attendance=85):
    """Read student data, process grades, and write results."""
    results = []

    try:
        with open(input_file, 'r') as file:
            print(f"Opened file: {input_file}")  # Debug: Confirm file opened
            for line_number, line in enumerate(file, 1):
                print(f"Processing line {line_number}: {line.strip()}")  # Debug
                try:
                    name, score = line.strip().split(',')
                    score = float(score)
                    print(f"Parsed: name={name}, score={score}")  # Debug

                    if not (0 <= score <= 100):
                        print(f"Invalid score {score} for {name}. Skipping.")  # Debug
                        continue

                    grade = calculate_grade(score)
                    passing = is_passing(score, attendance)
                    print(f"Result: name={name}, grade={grade}, passing={passing}")  # Debug

                    results.append((name, score, grade, "Pass" if passing else "Fail"))

                except ValueError as e:
                    print(f"Line {line_number}: ValueError - {e}")  # Debug
                except Exception as e:
                    print(f"Line {line_number}: Unexpected error - {e}")  # Debug

        with open(output_file, 'w') as file:
            print(f"Writing to {output_file}")  # Debug
            file.write("Name,Score,Grade,Status\n")
            for name, score, grade, status in results:
                file.write(f"{name},{score:.1f},{grade},{status}\n")

        print("Processing complete.")  # Debug

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")  # Debug
    except PermissionError:
        print(f"Error: Cannot access files.")  # Debug
    except Exception as e:
        print(f"Unexpected error: {e}")  # Debug


# Run with sample input
if __name__ == "__main__":
    process_student_data("students.txt", "grades.txt")