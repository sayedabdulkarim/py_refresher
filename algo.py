
def print_numbers_up_to(n):
    for i in range(n):
        print(i)

print_numbers_up_to(10)

# 
def concatenate_strings(str1, str2):
    return str1 + str2

print(concatenate_strings("Hello, ", "world!"))

# 
def sum_of_list(numbers):
    return sum(numbers)

print(sum_of_list([1, 2, 3, 4, 5]))

# 
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("radar"))  # Returns True
print(is_palindrome("python"))  # Returns False

# 
def find_max_min(numbers):
    return max(numbers), min(numbers)

print(find_max_min([3, 1, 4, 6, 5, 2]))

# 
def count_occurrences(lst, element):
    return lst.count(element)

print(count_occurrences([1, 2, 2, 3, 4, 4, 4], 4))  # Should return 3
