def reverse_string(s):
    return print(s[::-1])

#reverse_string('ślimak kamil')

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()     #filter retains only the elements from the array that are True filter(function, iterable)
    return print(s == s[::-1])

# is_palindrome('kamil!?slimak')

# my_tuple = (10, 20, 30)
# print(20 in my_tuple)    # Output: True
# print(40 in my_tuple)    # Output: False
# print(40 not in my_tuple) # Output: True

# my_tuple = (50, 10, 30, 20)
# sorted_tuple = sorted(my_tuple) # default return list, tuple() to return tuple
# print(sorted_tuple)

# my_list.sort(key=lambda arg : fun, reverse=True)
# new_list = sorted(my_list, key=lambda arg : fun, reverse=True)

# reversed_tuple = tuple(reversed(my_tuple))
    
# element's modification after created tuple wile rise a TypeError

# the way to modify the tuple:
# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)  # Convert to a list
# my_list[0] = 10           # Modify the list
# my_tuple = tuple(my_list)  # Convert back to a tuple
# print(my_tuple)          # Output: (10, 2, 3)

# my_tuple = (1, 2, 2, 3, 2)
# print(my_tuple.count(2))   # Output: 3
# print(my_tuple.index(3))   # Output: 3
# print(my_tuple[3])   # Output: 3

def count_vowels(s):
    vowels = 'aąeęiyou'
    count = 0
    for l in s:
        if l in vowels:
            count += 1
    return print(count)

# count_vowels("akamai")

from typing import List

def find_max(nums: List[int]) -> int:
    if not nums:
        return None
    
    max_num = nums[0]
    
    for n in nums:
        if n > max_num:
            max_num = n
    return print(max_num)

# listonosz = [1, 2, 9, 5]
# find_max(listonosz)

def is_even(nums: List[int]) -> List[int]:
    if not nums:
        return None
    
    even_list = [n for n in nums if n%2==0]
    return print(even_list)

# listonosz = [1, 2, 9, 5, 2, 4]
# is_even(listonosz)

def remove_duplicates(nums: List[int]) -> List[int]:
    return print(list(set(nums)))

# remove_duplicates(listonosz)


def fibonacci_generator(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fibonacci_array_generator(n: int) -> list[int]:
    return list(fibonacci_generator(n))

# print(fibonacci_array_generator(1)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fibo_generator(n : int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
def print_fibo(n: int) -> List[int]:
    return 0 if n == 0 else list(fibo_generator(n))

#print(print_fibo(10))


def fibo_recu(n: int, fib_list: List[int]) -> List[int]:
    if n == 2:
        return fib_list
    else:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
        return fibo_recu(n - 1, fib_list)
    
# print(fibo_recu(10, [0,1]))



def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        print(i)
        result *= i
    return result

#print(factorial(5))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# the num is prime when the num has not any other common factor lesser than its root + 1 
# print(is_prime(12))

def char_in_word_freq(s: str):
    dict = {}
    for char in s:
        dict[char] = dict.get(char, 0) + 1
    return dict
# print(char_in_word_freq('fall in love agin!'))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# print(gcd(26, 13))
