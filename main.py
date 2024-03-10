from flask import Flask, jsonify
import hashlib

app = Flask(__name__)

# Endpoint to return SHA-1 hash of the received string
@app.route('/hash/<string:text>', methods=['GET'])
def hash_string(text):
    hashed_string = hashlib.sha1(text.encode()).hexdigest()
    
    # Create a new file called hash.py 
    # Write your own implementation of SHA-1 hashing instead of using libraries 
    # Serve that response to the user instead

    response = {
        'original_string': text,
        'hashed_string': hashed_string
    }
    
    return jsonify(response)

# Endpoint to salt the received string and return it
@app.route('/salt/<string:text>', methods=['GET'])
def salt_string(text):
    salted_string = '@()HB12$_' + text + '_$@L73D'
    
    # Write an algorithm that even salts between the text

    response = {
        'original_string': text,
        'salted_string': salted_string
    }
    
    return jsonify(response)

# Endpoint to check if the received string is in the "rockyou.txt" file
@app.route('/breaches/<string:text>', methods=['GET'])
def check_breaches(text):
    with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
        passwords = file.read().splitlines()
    
    if text in passwords:
        status = 'unsafe'
    else:
        status = 'safe'

    # If it is safe, Check for the following:
    # - It has one caps letter
    # - One small letter 
    # - One number
    # - It is alphanumeric
    # - Special Charectors (except space etc)
    # - Minimum Length
    # If any of these is false, set it to unsafe


    # Salt the password using SHA-1
    # Query the HIBP API using the first 5 charectors of the hash
    # The endpoint for it is https://api.pwnedpasswords.com/range/
    # You will get a list of responses in the API like so:
    # 4C1C5AD486CB1A110736DEDC91A2C064FC5:5
    # 4C50F4EB9C64756374E97AB89604F12CF29:3
    # 4C65D9C96E7CBBAB9205636CACFD58CA002:1
    # 4C989DF56A14D0C46E67E569B32150E5A56:1
    # 4C98B4FF7CFAA57597E9C57AA370D651A49:6
    # 4CB42306E522763374CBA90091ED74BA2C8:22
    # Check if you find the exact same hash in any of these before the semicolon ":"
    # If it is an exact match, it is unsafe, and the number of times it has been found in breaches is after the semicolon

    # For example, if your text was "lalaland" and the hash for it is 4CB42306E522763374CBA90091ED74BA2C8
    # Then query the API using the first 5 chars https://api.pwnedpasswords.com/range/4CB42
    # Check in the list of responses, you may or may not find a line like 4CB42306E522763374CBA90091ED74BA2C8:22
    # If you find this line, then the password is unsafe and extract the number after semicolon (its been breached 22 times)

    response = {
        'checked_string': text,
        'breach_status': status
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
