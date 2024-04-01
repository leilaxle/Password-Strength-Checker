import random
import string

def generate_strong_password():
    length = int(input("Enter the length of the password: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated strong password:", password)

def check_password_strength(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': any(char.isupper() for char in password),
        'digit': any(char.isdigit() for char in password),
        'special_char': any(char in string.punctuation for char in password)
    }

    if all(criteria.values()):
        return "Very Strong"
    elif criteria['length'] and criteria['uppercase'] and criteria['digit']:
        return "Strong"
    elif criteria['length'] and criteria['uppercase']:
        return "Semi Strong"
    elif criteria['length']:
        return "Weak"
    else:
        return "Not Very Strong"

def main():
    while True:
        print("Hello user! A strong password is extremely important in being able to safeguard your information.")
        print("This tool is meant to help you assess the strength of your password and give you strong password recommendations at a click of a button.")
        print("Which option would you like to do? Type the number in.")
        choice = input("[1] Password Strength Checker, [2] Strong Password Generator, or [3] Quit: ")

        if choice == '1':
            user_password = input("Enter the password you want to check: ")
            strength = check_password_strength(user_password)
            print("Password strength:", strength)
        elif choice == '2':
            generate_strong_password()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose either 1, 2, or 3.")

        another_attempt = input("Do you want to check another password, generate another strong password, or go back to the menu? (yes/no/menu): ").lower()
        if another_attempt == 'no':
            print("Exiting the program. Goodbye!")
            break
        elif another_attempt == 'menu':
            continue

if __name__ == "__main__":
    main()
