#!/usr/bin/python
import getpass
import hashlib
import datetime

# our test system only has one user and one hashed pin for it
s_user = "utz"
# Calculate the MD5 hash of the PIN and store it as a hexdigest
s_hashed_pin = hashlib.md5("1234".encode()).hexdigest()

# check if user and hashed password match
def login(user, pin):
    if s_user == user and hashlib.md5(pin.encode()).hexdigest() == s_hashed_pin:
        return True
    else:
        return False

# Function to calculate time interval in milliseconds
def millis_interval(start, end):
    diff = end - start
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return str(millis) + " ms"

# Measure execution time
start = datetime.datetime.now()

# Bruteforce all possible PIN combinations
for pin_guess in range(10000):
    pin_guess_str = str(pin_guess).zfill(4)  # Convert pin_guess to 4-digit string
    if login(s_user, pin_guess_str):
        print(f"Access granted with PIN: {pin_guess_str}")
        break
else:
    print("No matching PIN found.")

stop = datetime.datetime.now()
print("Time to execute code:", millis_interval(start, stop))
