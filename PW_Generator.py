# TODO: Do an API check against HIBP. If the generated password is leaked, generate a new one before printing it.
# TODO: Move the password generation logic into a separate function.


import random
import secrets
import string

# Password generator


def input_valid_int(question, error_message):
    """Prompt the user until they enter a positive integer."""
    while True:
        length = input(question)
        if length.isdigit() and length != '0':
            return int(length)
        else:
            print(error_message)


def input_valid_string(question, error_message, possible_answers):
    """Prompt the user until they enter one of the allowed answers."""
    while True:
        answer = input(question).lower()
        if answer in possible_answers:
            return answer
        else:
            print(error_message)


def get_allowed_chars(lower, upper, numbers, characters):
    """Return a list of character sets based on the user's choices."""
    sets = []
    if lower == 'y' or lower == "yes":
        sets.append(lowercase)
    if upper == 'y' or upper == "yes":
        sets.append(uppercase)
    if numbers == 'y' or numbers == "yes":
        sets.append(digits)
    if characters == 'y' or characters == "yes":
        sets.append(special_characters)
    return sets


def generate_password(allowed_chars, length):
    """Generates the password and returns it."""
    # Include at least one character from each selected character set
    required_chars = []
    for charset in allowed_chars:
        random_char = secrets.choice(charset)
        required_chars.append(random_char)

    # Combine all selected character sets into a single pool for random picks
    allowed_chars_joined = ''.join(allowed_chars)

    # Already added one required character per set, fill the remaining length
    new_length = length - len(required_chars)

    # Fill remaining password length with random allowed characters
    password = []
    for i in range(new_length):
        random_allow = secrets.choice(allowed_chars_joined)
        password.append(random_allow)

    password.extend(required_chars)
    random.shuffle(password)
    password = ''.join(password)
    return password


# a-z, A-Z, 0-9 and common special characters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Controls whether we ask for new settings or reuse the previous ones
new_settings = True

print('Welcome to the password generator!\n')

# Main loop: read settings (once) and generate passwords

while True:
    if new_settings:
        length = input_valid_int(
            'Enter password length: ',
            'Error: Enter a positive number greater than 0!')
        numbers = input_valid_string(
            'Should numbers be included? (y/n): ',
            'Error: Enter "y" or "n"',
            ('y', 'yes', 'no', 'n'))
        characters = input_valid_string(
            'Should special characters be included? (y/n): ',
            'Error: Enter "y" or "n"',
            ('y', 'yes', 'no', 'n'))
        lower = input_valid_string(
            'Should lowercase letters be included? (y/n): ',
            'Error: Enter "y" or "n"',
            ('y', 'yes', 'no', 'n'))
        upper = input_valid_string(
            'Should capital letters be included? (y/n): ',
            'Error: Enter "y" or "n"',
            ('y', 'yes', 'no', 'n'))

        # Minimum length based on number of selected character sets
        allowed_chars = get_allowed_chars(lower, upper, numbers, characters)
        min_length = len(allowed_chars)

        if min_length == 0:
            print(
                'Error: You need to choose at least one letter, number or special character!')
            continue

        if length < min_length:
            print(
                f'Error: With your choices, the password needs to be at least {min_length} characters.')
            continue

    new_settings = False

    password = generate_password(allowed_chars, length)
    print(password)

    # Ask if the user wants to generate another password with the same settings
    new_password = input_valid_string(
        '\nDo you want to generate a new password using the same settings? (y/n): ',
        'Error: Enter "y" or "n"',
        ('y', 'yes', 'n', 'no'),
    ).lower()

    if new_password == 'n' or new_password == "no":
        break
