def remove_even_numbers(numbers):
    """
    Returns a new list with even numbers removed. 
    Using list comprehension is the professional approach to avoid the common bug 
    of modifying a list while iterating over it.
    """
    return [number for number in numbers if number % 2 != 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_list)

print(f"Original list: {my_list}")
print(f"List after removing even numbers: {result}")