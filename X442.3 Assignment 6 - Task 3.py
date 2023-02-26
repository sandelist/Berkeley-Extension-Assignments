# Task 3

# Suppose the constant is 8

def addition_contants(n):
    return n + 8

# Suppose the list is [1, 20, 300, 400]

numbers = [1, 20, 300, 400]

result = map(addition_contants, numbers)

print(list(result))

# Performing contants addition with list comprehension:

numbers = [1, 20, 300, 400]

new_results = [x + 8 for x in numbers]

print(new_results)