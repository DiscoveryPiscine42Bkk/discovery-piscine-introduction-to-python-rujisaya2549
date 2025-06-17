original_numbers = [1, 2, 3, 4, 5, 3, 4]
new_numbers = [num + 2 for num in original_numbers]
new_numbers = [num for num in new_numbers if num > 5]
unique_numbers = []
for num in new_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Original array:", original_numbers)
print("New array (only unique values > 5):", unique_numbers)
