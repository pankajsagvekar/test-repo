def remove_even_numbers(numbers):
    """
    Returns a new list containing only the odd numbers from the input list.
    Avoids modifying the list while iterating by using a list comprehension.
    """
    return [number for number in numbers if number % 2 != 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_list)

print(f"Original list: {my_list}")
print(f"List after removing even numbers: {result}")