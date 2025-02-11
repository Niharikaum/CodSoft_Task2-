# -*- coding: utf-8 -*-
"""task_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10gDhHFRB4UIg3rFC3yhsaWRCineLYdoe
"""

import random
import string

# Function to generate a password
def generate_password(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Main program
length = int(input("Enter the desired password length (minimum 6): "))
if length < 6:
    print("Password length should be at least 6 characters.")
else:
    password = generate_password(length)
    print(f"Generated Password: {password}")