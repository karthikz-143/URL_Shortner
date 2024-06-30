# URL_Shortner

Project Outline
Aim:
Develop a URL shortener that takes a long URL as input and generates a shortened version.

Description:
Create a Python script that interacts with a URL shortening service or uses a custom algorithm to generate short URLs. The script should take a long URL as input and output the corresponding shortened URL.

Technologies:
Python

What You Learn:

String manipulation and algorithms
Input handling
Detailed Steps
Step 1: Choose a URL Shortening Method
Using a URL Shortening Service: Utilize APIs like Bitly or TinyURL.
Custom Algorithm: Implement a simple algorithm to map long URLs to short ones (e.g., using a hash function or an incrementing ID).
Tip: For a custom algorithm, you might want to store mappings in a dictionary or a database to keep track of original and shortened URLs.

Step 2: Implement the URL Shortening Logic
Option 1: Using Bitly API

Sign up for Bitly and get an API key.
Use the requests library to interact with the Bitly API.
Option 2: Custom Algorithm

Create a function to generate a short URL.
Store mappings of original and short URLs.
Step 3: Handle User Input
Prompt the user to enter a long URL and return the shortened URL.

Step 4: Display the Shortened URL
Print the shortened URL to the user.
