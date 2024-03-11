from flask import Flask, jsonify
import hashlib
import re
import requests

app = Flask(__name__)

# Endpoint to return SHA-1 hash of the received string
@app.route('/hash/<string:text>', methods=['GET'])
def hash_string(text):
    hashed_string = hashlib.sha1(text.encode()).hexdigest()

    response = {
        'original_string': text,
        'hashed_string': hashed_string
    }
    
    return jsonify(response)

# Endpoint to salt the received string and return it
@app.route('/salt/<string:text>', methods=['GET'])
def salt_string(text):
    salted_string = '@()HB12$_' + text + '_$@L73D'
    
    # TODO: Task 2
    # Write an algorithm that even salts between the text

    response = {
        'original_string': text,
        'salted_string': salted_string
    }
    
    return jsonify(response)

@app.route('/strength/<string:text>', methods=['GET'])
def check_breaches(text):
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
        passwords = file.read().splitlines()

    potential_issues = []

    # Check if the text is found in the "rockyou.txt" file
    if text in passwords:
        potential_issues.append("Found in common passwords list")

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in text):
        potential_issues.append("No uppercase letter")

    # Check for at least one lowercase letter
    if not any(char.islower() for char in text):
        potential_issues.append("No lowercase letter")

    # Check for at least one digit
    if not any(char.isdigit() for char in text):
        potential_issues.append("No digit")

    # Check for at least one special character (except space)
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', text):
        potential_issues.append("No special character")

    # Check for minimum length of 8
    if len(text) < 8:
        potential_issues.append("Length less than 8 characters")

    # Determine the overall status
    if potential_issues:
        status = 'unsafe'
    else:
        status = 'safe'

    response = {
        'checked_string': text,
        'breach_status': status,
        'potential_issues': potential_issues
    }

    return jsonify(response)

        

@app.route('/check_hibp/<string:text>', methods=['GET'])
def check_hibp(text):
    # Salt the password using SHA-1
    hashed_text = hashlib.sha1(text.encode()).hexdigest()

    # Query the HIBP API using the first 5 characters of the hash
    api_url = f'https://api.pwnedpasswords.com/range/{hashed_text[:5]}'
    response = requests.get(api_url)

    if response.status_code == 200:
        # Check if the exact hash match is found in the API responses
        hash_suffix = hashed_text[5:].upper()
        breached_count = 0

        for line in response.text.splitlines():
            if line.startswith(hash_suffix):
                # If the exact hash match is found, extract the number of times it has been breached
                breached_count = int(line.split(':')[1])
                break

        if breached_count > 0:
            status = 'unsafe'
            response_message = f'The password has been breached {breached_count} times.'
        else:
            status = 'safe'
            response_message = 'The password is not found in breaches.'

    else:
        # Handle API request failure
        status = 'error'
        response_message = 'Error connecting to HIBP API.'

    response = {
        'checked_string': text,
        'hibp_status': status,
        'message': response_message
    }

    return jsonify(response)

    
if __name__ == '__main__':
    app.run(debug=True)
