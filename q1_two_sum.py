# Name: Prashant Kumar
# UID: 22BCS15537
# Course: Advanced Programming Lab (AP Lab)
# Semester: 6th Semester
# Problem: Two Sum
# Question Number: Q1
# Description: Return indices of two numbers that add up to a specific target

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print("Indices:", two_sum(nums, target))  # Output: [0, 1]
