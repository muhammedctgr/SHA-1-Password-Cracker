# SHA-1-Password-Cracker
# This is the boilerplate for the SHA-1 Password Cracker project, part of FCC Information Security Certification Projects.
[![Run on Repl.it](https://repl.it/badge/github/muhammedctgr/SHA-1-Password-Cracker)](https://replit.com/@6ix-Ville/boilerplate-SHA-1-password-cracker)

In this project I learn about the importance of good security by creating a password cracker to figure out passwords that were hashed using SHA-1.

A function that takes in a SHA-1 hash of a password and returns the password if it is one of the top 10,000 passwords used. If the SHA-1 hash is NOT of a password in the database, it returns "PASSWORD NOT IN DATABASE".

The function should hash each password from top-10000-passwords.txt and compare it to the hash passed into the function.

The function should take an optional second argument named use_salts. If set to true, each salt string from the file known-salts.txt should be appended AND prepended to each password from top-10000-passwords.txt before hashing and before comparing it to the hash passed into the function.
