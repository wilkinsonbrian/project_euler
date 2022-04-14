def find_primes():
    primes = []
    starting = [x for x in range(2, 1000000)]
    while len(starting) > 0:
        primes.append(starting[0])
        testing = starting[0]
        for number in starting:
            if number % testing == 0:
                starting.remove(number)

    return primes

def get_prime_factors(primes, number):
    factors = []
    for x in primes:
        while number % x == 0:
            number /= x
            if x not in factors:
                factors.append(x)
        if number == 0:
            break
    return len(factors)


def main():
    list_of_primes = find_primes()
    for x in range(330, 500000):
        if get_prime_factors(list_of_primes, x) == 4 and get_prime_factors(list_of_primes, x + 1) == 4 and get_prime_factors(list_of_primes, x + 2) == 4 and get_prime_factors(list_of_primes, x + 3) == 4:
            print(x)
            break

if __name__ == '__main__':
    main()

