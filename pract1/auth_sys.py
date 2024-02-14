#!/usr/bin/python
import getpass

# our test system only has one user and one pin for it
s_user="utz"
s_pin="1234"

# check if user and password match
def login(user,pin):
    if s_user==user and s_pin==pin:
        print("user/PIN:"+user+"/"+pin)
        return True
    else:
        return False
    
# ask for the username and password
user=input("user:")
pin=getpass.getpass("PIN:")
# check if we can log in
if login(user,pin):
    print("access granted")
else:
    print("access denied")
    