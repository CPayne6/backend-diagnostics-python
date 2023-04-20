import math

def find_primes(max_number):
    """
        Creates a list of all prime numbers less than max_number using atkin algorithm

        :param max_number: number to stop finding primes at
    """

    arr = [False] * (max_number + 1)

    k = int(math.sqrt(max_number)) + 1

    for x in range(1, k):
        for y in range(1, k):
            n = 4 * x ** 2 + y ** 2
            if n <= max_number and (n % 12 == 1 or n % 12 == 5):
                arr[n] = not arr[n]
            
            n = 3 * x ** 2 + y ** 2
            if n <= max_number and n % 12 == 7:
                arr[n] = not arr[n]
            
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= max_number and n % 12 == 11:
                arr[n] = not arr[n]

            y += 1
        x += 1

    # Eliminate squares and multiples of squares
    for r in range(5, k):
        if arr[r]:
            i = 1
            while (i * r ** 2 <= max_number):
                arr[i * r ** 2] = False
                i += 1
        r += 1

    primes = [index for index in range(max_number + 1) if arr[index]]

    if max_number >= 3:
        primes.insert(0, 3)
    if max_number >= 2:
        primes.insert(0, 2)

    return primes
