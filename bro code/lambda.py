# Lambda function = A small anonymous function for a one time use
#                  Then throw it away(throw away function)

#                  They take any number of arguments, but have only 1 expression

#                  Helps keep the namespace clean and is useful with higher-order functions
#                  'sort()', 'map()', 'filter()', 'reduce()'

#                   Syntax- lambda parameters: expression



double = lambda x: x * 2
print(double(2))

add = lambda x, y: x + y
print(add(3, 4))

max_value = lambda x, y: x if x > y else y
print(max_value(6, 7))

min_value = lambda x, y: x if x < y else y
print(min_value(9, 8))

full_name = lambda first, last: first + " " + last
print(full_name("Spongebob", "Squarepants"))

is_even = lambda x: x % 2 == 0
print(is_even(5))

age_check = lambda age: True if age >= 18 else False
print(age_check(21))














