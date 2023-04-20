import math

def find_primes(max_number):
    """
        Creates a list of all prime numbers less than max_number using eratosthenes algorithm

        :param max_number: number to stop finding primes at
    """
    # Initialize array of true values of length max_number
    arr = [True] * (max_number)
    arr[0] = False
    arr[1] = False
    i = 2
    while i < math.sqrt(max_number):
        if arr[i]:
            j = i ** 2
            while j < max_number:
                arr[int(j)] = False
                j += i
        i += 1

    
    return [index for index in range(max_number) if arr[index]]
