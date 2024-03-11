# Password Manager API Server

This project is a flask server that offers endpoints for the following:
- Hashing Passwords
- Salting Passwords
- Checking for Breaches

It uses the following third party APIs using a K-Anonymity model to ensure that the data is safe in transit and not entirely exposed to third parties:
- HIBP API 

And it uses the following breaches databases to check for unsafe passwords:
- RockYou

## Usage 

For cloning this repo from GitHub and installing dependencies:

```
    git clone https://github.com/pratz10101/dataprivacy-project-api.git
    pip install requirements.txt
```

For starting the server:
```
    python main.py
```

You can also use docker to run this project with the Dockerfile added

## API Documentation

The base URL for this API is `http://localhost:5000/` when running locally. Please replace it with the appropriate URL when deploying the API.

### 1. Hash a String

#### Endpoint
```
GET /hash/<string:text>
```

#### Description
This endpoint returns the SHA-1 hash of the received string.

#### Request
- Method: `GET`
- URL Parameters:
  - `text` (string): The input string to be hashed.

#### Response
```json
{
  "original_string": "input_string",
  "hashed_string": "hashed_output"
}
```

### 2. Salt a String

#### Endpoint
```
GET /salt/<string:text>
```

#### Description
This endpoint salts the received string and returns the salted string.

#### Request
- Method: `GET`
- URL Parameters:
  - `text` (string): The input string to be salted.

#### Response
```json
{
  "original_string": "input_string",
  "salted_string": "@()HB12$_salted_input_$@L73D"
}
```

### 3. Check for Password Breaches

#### Endpoint
```
GET /breaches/<string:text>
```

#### Description
This endpoint checks if the received string has been compromised in common password breaches. It performs several checks, including common passwords, uppercase and lowercase letters, digits, special characters, and minimum length.

#### Request
- Method: `GET`
- URL Parameters:
  - `text` (string): The password to be checked for breaches.

#### Response
```json
{
  "checked_string": "input_password",
  "breach_status": "safe/unsafe",
  "potential_issues": ["Issue 1", "Issue 2", ...]
}
```

### 4. Check HIBP (Have I Been Pwned) for Password Breaches

#### Endpoint
```
GET /check_hibp/<string:text>
```

#### Description
This endpoint checks if the received password has been breached using the Have I Been Pwned (HIBP) API. It salts the password using SHA-1 and queries the HIBP API to determine if the password has been compromised.

#### Request
- Method: `GET`
- URL Parameters:
  - `text` (string): The password to be checked for breaches.

#### Response
```json
{
  "checked_string": "input_password",
  "hibp_status": "safe/unsafe/error",
  "message": "The password is not found in breaches./The password has been breached n times./Error connecting to HIBP API."
}
```
