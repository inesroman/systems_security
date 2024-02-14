#!/usr/bin/python
import getpass
import hashlib
import itertools
import datetime
import os

# Recursive hash function
def recursive_hash(pin, iterations):
    hashed_pin = pin
    for _ in range(iterations):
        hashed_pin = hashlib.md5(hashed_pin.encode()).hexdigest()
    return hashed_pin

# Function to generate hash table and write it to a file if the file doesn't exist
def generate_hash_table(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            for pin in range(10000):
                pin_str = str(pin).zfill(4)
                hashed_pin = recursive_hash(pin_str, 10000)
                file.write(f"{pin_str}:{hashed_pin}\n")
    else:
        print("Hash table file already exists. Skipping generation.")


# Function to read hash table from file
def read_hash_table(file_path):
    hash_table = {}
    with open(file_path, 'r') as file:
        for line in file:
            pin, hashed_pin = line.strip().split(':')
            hash_table[pin] = hashed_pin
    return hash_table

# Function to calculate time interval in milliseconds
def millis_interval(start, end):
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return str(millis) + " ms"

# check if user and hashed password match
def login(user, pin, hash_table):
    return user == s_user and pin in hash_table and hash_table[pin] == s_hashed_pin

# our test system only has one user
s_user = "utz"
# Calculate the MD5 hash of the PIN and store it as a hexdigest
s_hashed_pin = recursive_hash("1234", 10000)

# Generate hash table and write it to a file
generate_hash_table("hash_table.txt")

# Read hash table from file
hash_table = read_hash_table("hash_table.txt")

# Measure execution time
start = datetime.datetime.now()

# Bruteforce all possible PIN combinations
for pin_guess in range(10000):
    pin_guess_str = str(pin_guess).zfill(4)  # Convert pin_guess to 4-digit string
    if login(s_user, pin_guess_str, hash_table):
        print(f"Access granted with PIN: {pin_guess_str}")
        break
else:
    print("No matching PIN found.")

stop = datetime.datetime.now()
print("Time to break code using generated file:", millis_interval(start, stop))
