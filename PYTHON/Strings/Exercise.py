
""" 
- indexing, slicing, upper(), lower(), replace(), split(), strip(), f-strings
 Exercises:
 1. Print the first character.
 2. Print the last character.
 3. Convert to uppercase.
 4. Count characters.
 5. Reverse a string. 
"""

str = "Hello , This is Rakshya Bhuju , Money comes to me easily , Money comes to me fasttt !!!!"

# Printing out the very first character
print(str[0]) 

# Print the last character
print(str[-1])

# Convert to uppercase
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())


# Count the characters
print(len(str))

# Reverse a string
print(str[::-1])

val = ''.join(reversed(str))
print(val)
