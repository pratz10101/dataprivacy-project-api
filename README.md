# Password Manager API Server

This project is a flask server that offers endpoints for the following:
- Hashing Passwords
- Salting Passwords
- Checking for Breaches

It uses the following third party APIs using a K-Anonymity model to ensure that the data is safe in transit and not entirely exposed to third parties:
- HIBP API 

And it uses the following breaches databases to check for unsafe passwords:
- RockYou
