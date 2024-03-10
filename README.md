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

### `/hash/<string:text>` (GET)
This endpoint takes a text value in the URL path and returns the SHA-1 hash of the provided string.

#### Example Request:
```
GET /hash/mytext
```

#### Example Response:
```json
{
  "original_string": "mytext",
  "hashed_string": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
}
```

---

### `/salt/<string:text>` (GET)
This endpoint takes a text value in the URL path, salts the string, and returns the result.

#### Example Request:
```
GET /salt/mytext
```

#### Example Response:
```json
{
  "original_string": "mytext",
  "salted_string": "mytext_SALT"
}
```

---

### `/breaches/<string:text>` (GET)
This endpoint takes a text value in the URL path and checks if it exists in the "rockyou.txt" file, indicating a potential security breach.

#### Example Request:
```
GET /breaches/password123
```

#### Example Response (if found in the file):
```json
{
  "checked_string": "password123",
  "breach_status": "unsafe"
}
```

#### Example Response (if not found in the file):
```json
{
  "checked_string": "securepassword",
  "breach_status": "safe"
}
```
