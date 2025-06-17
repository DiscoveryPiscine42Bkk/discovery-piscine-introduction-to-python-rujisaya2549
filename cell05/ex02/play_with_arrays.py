original_numbers = [1, 2, 3, 4, 5]
new_numbers = [num + 2 for num in original_numbers]
new_numbers = [num for num in new_numbers if num > 5]
print("Original array:", original_numbers)
print("New array (only values > 5):", new_numbers)
