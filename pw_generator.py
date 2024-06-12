import random
import string

# creating function to generate password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters = characters + digits
        if special_characters:
            characters = characters + special

        password = ""
        meets_criteria = False
        has_number = False
        has_special = False

        while not meets_criteria or len(password) < min_length:
            new_characters = random.choice(characters)
            password = password + new_characters

            if new_characters in digits:
                has_number = True
            elif new_characters in special:
                has_special = True

            meets_criteria = True
            if numbers:
                meets_criteria = has_number
            if special_characters:
                meets_criteria = meets_criteria and has_special

        return password


min_length = int(input("Enter minimum password length: "))
has_number = input("Numbers on password? (yes/no): ").lower() == "yes"
has_special = input("Special characters on password? (yes/no): ").lower() == "yes"
pwd = generate_password(min_length, has_number, has_special)
print(f"Thank you for your patience user, new password is {pwd}!")