#!/usr/bin/python
import getpass
import hashlib
import os

# our test system only has one user
s_user = "utz"

# Function to generate a random salt
def generate_salt():
    return os.urandom(16).hex()[:4]  # Generating a 4-character hexadecimal salt

# Function to generate hashed password with salt
def hash_with_salt(pin, salt):
    return hashlib.md5((pin + salt).encode()).hexdigest()

# Function to authenticate user
def login(user, pin, hashed_pin, salt):
    return user == s_user and hash_with_salt(pin, salt) == hashed_pin

# Ask for the username
user = input("user:")

# Generate a random salt
salt = generate_salt()

# Ask for the PIN
pin = getpass.getpass("PIN:")

# Calculate the hashed PIN with salt
hashed_pin = hash_with_salt(pin, salt)

# Mocking the stored hashed PIN (you would load this from storage)
stored_hashed_pin = hash_with_salt("1234", salt)

# Check if we can log in
if login(user, pin, stored_hashed_pin, salt):
    print("access granted")
else:
    print("access denied")
