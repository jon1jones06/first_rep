from functools import reduce

numbers = [1,2,3,4,5]

squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", even)

sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum_numbers)