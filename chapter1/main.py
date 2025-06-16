import random

#R-1.1
def is_multiple(n, m):
    if n % m == 0:
        return True
    return False

#R-1.2
def is_even(k):
    if ((k & 1) == 0):
        return True
    return False

#R-1.3
def minmax(data):
    min_data = float('inf')
    max_data = float('-inf')
    
    for num in data:
        if num < min_data:
            min_data = num
        if num > max_data:
            max_data = num
    return (min_data, max_data)

#R-1.4
def positive_integer(n):
    if n < 0:
        return None
    
    suma = 0
    for i in range(1, n):
        suma += (i ** 2)

    return suma

#R-1.5
def positive_integer_built_in(n):
    return sum([x ** 2 for x in range(1, n)])

#R-1.6
def positive_odd(n):
    suma_odd = 0
    
    for i in range(1, n):
        if ((i & 1) == 1):
            suma_odd += (i ** 2)
    
    return suma_odd

#R-1.7 
def positive_sum_odd(n):
    return sum([x ** 2 for x in range(1, n) if x & 1 == 1])

#R-1.8
#j = n + k
#That's how'd you get the same index on j and k. My English is not good.

#R-1.9
def parameter():
    return range(50, 90, 10)

#R-1.10
def para():
    return range(8, -9, -2)

#R-1.11
def list_comprehension():
    return [2 ** x for x in range(0, 10)] 

#R-1.12
def random_number(data):
    rand_idx = random.randrange(len(data))
    return data[rand_idx]

#C-1.13 Pseudo-Code. I'll not do it.

#C-1.14
def sequence_integer(n):
    count = 0

    for i in range(0, len(n)):
        if n[i] & 1 == 1:
            count += 1
    
    if count >= 2:
        return True
    else:
        return False
#C-1.15
def seq_numbers(number):
    dict1 = {}

    for n in number:
        if n in dict1:
            dict1[n] += 1
        else:
            dict1[n] = 0

    for key in dict1:
        if dict1[key] > 0:
            return True
       
    return False

#C-1.16 Lists are mutable.
#C-1.17 Is not correct. Cause it modifies the local variable named "val", but no the values of the array.

#C-1.18
def lis_sum_two():
    return [ n * (n + 1) for n in range(10)]

#C-1.19
def lis_char():
    return [chr(x) for x in range(97, 123)]

ch = lis_char()
print(ch)

#C-1.20
#DEPRECATED

