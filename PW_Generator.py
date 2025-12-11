

import secrets
import string
import hashlib
import requests


# Password generator


def input_valid_int(question, error_message):
    """Prompt the user until they enter a positive integer."""
    while True:
        length = input(question)
        if length.isdigit() and int(length) > 0:
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
    if lower in ('y', 'yes'):
        sets.append(lowercase)
    if upper in ('y', 'yes'):
        sets.append(uppercase)
    if numbers in ('y', 'yes'):
        sets.append(digits)
    if characters in ('y', 'yes'):
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
    secrets.SystemRandom().shuffle(password)
    password = ''.join(password)
    return password


def hibp_check(password):
    """Check password against HIBP."""
    sha1_obj = hashlib.sha1(password.encode("utf-8"))
    sha1_hex = sha1_obj.hexdigest().upper()
    prefix = sha1_hex[:5]
    suffix = sha1_hex[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, timeout=3)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    body = response.text
    lines = body.splitlines()

    for line in lines:
        if line.startswith(suffix + ":"):
            # Password is pwned
            return True

    # If no leak was found
    return False


# a-z, A-Z, 0-9 and common special characters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = '!#$%&()*+,-./:;<=>?@[]^_{|}~'

# Controls whether we ask for new settings or reuse the previous ones
new_settings = True

print('Welcome to the password generator!\n')

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
        allowed_chars = get_allowed_chars(
            lower, upper, numbers, characters)
        min_length = len(allowed_chars)

        if min_length == 0:
            print(
                'Error: You need to choose at least one letter, number or special character!')
            continue

        if length < min_length:
            print(
                f'Error: With your choices, the password needs to be at least {min_length} characters.')
            continue

    # Generates the password and checks it against HIBP

    while True:
        password = generate_password(allowed_chars, length)

        print('\nWill now attempt to check the password against Haveibeenpwned, for any leaks online...')
        hibp = hibp_check(password)

        if hibp is None:
            print(
                '\nError: Failed to check if the password has been included in any leaks online. Please be aware!')
            break
        elif hibp is False:
            print('\nThe password was not found in any leaks online, congrats!')
            break
        else:
            print('\nThe generated password was found in leaks, generating a new one...')
            continue

    print(f'Password: {password}')

    # Ask if the user wants to generate another password
    new_password = input_valid_string(
        '\nHow would you like to proceed?\n'
        '[1] Generate a new password using the same settings.\n'
        '[2] Generate a new password using new settings.\n'
        '[3] Exit script.\n'
        'Choose an option: ',
        'Error: Choose an option 1-3',
        ('1', '2', '3'),
    ).lower()

    if new_password == '1':
        new_settings = False
    elif new_password == '2':
        new_settings = True
    else:
        break


print('Exiting...')
