"""
Generate a random 8-character password
using Python's built-in random and string modules.
"""

import random
import string

characters = string.ascii_letters + string.digits

password = ''.join(random.choice(characters) for _ in range(8))

print(f"Your generated password is: {password}")