#!/usr/bin/python
import getpass
import hashlib

# our test system only has one user and one hashed pin for it
s_user = "utz"
# Calculate the MD5 hash of the PIN and store it as a hexdigest
s_hashed_pin = hashlib.md5("1234".encode()).hexdigest()

# check if user and hashed password match
def login(user, pin):
    if s_user == user and hashlib.md5(pin.encode()).hexdigest() == s_hashed_pin:
        print("user/PIN:"+user+"/"+pin)
        return True
    else:
        return False
    
# ask for the username and password
user = input("user:")
pin = getpass.getpass("PIN:")

# check if we can log in
if login(user, pin):
    print("access granted")
else:
    print("access denied")
