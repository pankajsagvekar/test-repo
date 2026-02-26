def remove_even_numbers(numbers):
    # Use list comprehension to correctly filter out even numbers and avoid skipping elements
    return [number for number in numbers if number % 2 != 0]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_list)
print(f"Original list: {my_list}")
print(f"List after removing even numbers: {result}")
print(f"error remove from rohit's pc: {result}")