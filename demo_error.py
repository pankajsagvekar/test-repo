def remove_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
    return numbers

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(my_list)
print(f"Original list: {my_list}")
print(f"List after removing even numbers: {result}")
print(f"error remove from rohit's pc" {result}"
