# Name: Prashant Kumar
# UID: 22BCS15537
# Course: Advanced Programming Lab (AP Lab)
# Semester: 6th Semester
# Problem: Maximum Subarray
# Question Number: Q5
# Description: Find the contiguous subarray which has the largest sum

def max_subarray(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray(nums))  # Output: 6
