## Password generator is a Random Password generating program which generates a password mix of upper and lowercase letters, as well as numbers and symbols strong enough to provides great security.

import random
import string
# taking user input
length = int(input("Enter total length of password:"))

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

All = lower_case + upper_case + number + symbols

temp = random.sample(All, length)

password = "".join(temp)
print(password)