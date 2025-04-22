def get_user():
    name = input("What is your name?")

    while True:
        age_input = input("How old are you?")
        if age_input.isdigit():
            age = int(age_input)
            break
        else:
            print("Please enter a valid number for your age.")

    return name, age

def generate_greeting(name, age):
    if age < 13:
        return f"Hey there, {name}! You're quite young! Enjoy your childhood!"
    elif age<20:
        return f"What's up, {name}? Teenage years are wild, huh?"
    elif age<60:
        return f"Hello {name}! Hope your adulting is going well. Keep hustling!"
    else:
        return f"Namaste {name}. Wishing you health and happiness."

if __name__ == "__main__":
    user_name, user_age = get_user()
    greeting = generate_greeting(user_name, user_age)
    print(greeting)