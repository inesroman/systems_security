#!/usr/bin/python
import hashlib
import getpass
import os

# our test system only has one user
s_user = "utz"

# Function to generate a random salt
def generate_salt():
    return os.urandom(16)  # Generate a random 16-byte salt

# Function to hash password with salt using PBKDF2-HMAC
def hash_with_salt(pin, salt):
    # Use PBKDF2-HMAC with 10000 iterations and a key length of 32 bytes
    return hashlib.pbkdf2_hmac('sha256', pin.encode(), salt, 10000, dklen=32)

# Function to authenticate user
def login(user, pin, stored_hash, salt):
    # Calculate the hash of the provided PIN using the same salt and compare it with the stored hash
    return user == s_user and hashlib.pbkdf2_hmac('sha256', pin.encode(), salt, 10000, dklen=32) == stored_hash

# Ask for the username
user = input("user:")

# Generate a random salt
salt = generate_salt()

# Ask for the PIN
pin = getpass.getpass("PIN:")

# Calculate the hashed PIN with salt using PBKDF2-HMAC
hashed_pin = hash_with_salt(pin, salt)

# Mocking the stored hashed PIN (you would load this from storage)
stored_hashed_pin = hash_with_salt("1234", salt)

# Check if we can log in
if login(user, pin, stored_hashed_pin, salt):
    print("access granted")
else:
    print("access denied")
