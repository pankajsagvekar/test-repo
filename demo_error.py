def remove_even_numbers(numbers):
    """
    Returns a new list containing only the odd numbers.
    Note: Modifying a list while iterating over it (as in the original code) 
    causes elements to be skipped and results in logical instability.
    """
    return [number for number in numbers if number % 2 != 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_list)

print(f"Original list: {my_list}")
print(f"List after removing even numbers: {result}")