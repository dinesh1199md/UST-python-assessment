import re

def validate(passwords):
    # Regular expression pattern to validate the password
    pattern = re.compile(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$'
    )
    # Filter valid passwords
    valid_passwords = [password for password in passwords if pattern.match(password)]
    return valid_passwords

def validate_passwords():
    try:
        password_input_file = "input_data/password_validator_input.txt"
        with open(password_input_file, "r") as file:
            passwords = file.read().strip().split(',')
        valid_passwords = validate(passwords)
        print(f"Input_passwords : {passwords} \nValid passwords:", ', '.join(valid_passwords))
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print("Exception @validate_passwords:",e) 
