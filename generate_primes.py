def find_primes():
    primes = []
    starting = [x for x in range(2, 1000000)]
    while len(starting) > 0:
        primes.append(starting[0])
        testing = starting[0]
        for number in starting:
            if number % testing == 0:
                starting.remove(number)

    prime_file = open("primes.txt", "w")
    for y in primes:
        prime_file.write(str(y) + "\n")
    prime_file.close()

find_primes()