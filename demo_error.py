def remove_even_numbers(numbers):
    # Fixed the harmful logic: iterating over a list while modifying it causes items to be skipped.
    # Using a list comprehension is the clean, professional, and stable way to filter a list.
    return [number for number in numbers if number % 2 != 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_list)

print(f"Original list: {my_list}")
print(f"List after removing even numbers: {result}")
# Fixed Line 11: Corrected the f-string syntax and added missing closing parenthesis.
print(f"Final processed result: {result}")