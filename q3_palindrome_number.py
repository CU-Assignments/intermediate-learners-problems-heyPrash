# Name: Prashant Kumar
# UID: 22BCS15537
# Course: Advanced Programming Lab (AP Lab)
# Semester: 6th Semester
# Problem: Palindrome Number
# Question Number: Q3
# Description: Determine whether an integer is a palindrome

def is_palindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Example usage
number = 121
print("Is Palindrome?", is_palindrome(number))  # Output: True
