## Part 1
auth_sys.py codes a very simple system where we have exactly one user who is using a 4
digit Personal Authentication Number (PIN) as a password to log in.

## Part 2
Modification of the system in PART 1: passwords are not stored in clear text. We just save the hashes.

## Part 3
Modification of the program in PART 2. The user is not asked to input the user and the passowrd anymore, instead a routine tries all possible 4-digit PINS.

## Part 4
To prevent fast guessing of the PIN in PART 3, something needs to be done. We can make the hash function more computationally expensive. If it takes more effort to compute the hash, the time it takes to try PIN combinations increases. The hash function is replaced by a recursive hash function calling itself 10000 times.

## Part 5
Instead of computing all hash values on the fly, we write a program that writes all these in a file. Then the program reads and tries to login with all the PINS in the file.

## Part 6
Modification of the original program, storing the hash of the password and a random salt of 4 digits.

## Part 7
Modification of the program in PART 6 using the function pbkdf2 hmac() of the hashlib library.