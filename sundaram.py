def find_primes(max_number):
    """
        Creates a list of all prime numbers less than max_number using sundaram algorithm

        :param max_number: number to stop finding primes at
    """

    k = (max_number - 2) // 2
    arr = [True] * (k + 1)
    arr[0] = False
    i = 1
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            arr[i + j + 2 * i * j] = False
            j += 1
    
    primes = [index * 2 + 1 for index in range(k + 1) if arr[index]]
    if max_number >= 2:
        primes = [2] + primes

    return primes
