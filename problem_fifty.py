prime_file = open("primes.txt", "r")
primes = []
for line in prime_file.readlines():
    primes.append(int(line[:-1]))

chain = 0
max_sum = 0

for p in primes:
    total = 0
    length = 0
    x = primes.index(p)
    while total < 1000000:
        total += primes[x]
        length += 1
        if total in primes:
            if length > chain:
                chain = length
                max_sum = total
                print(max_sum)
        x += 1
print(max_sum)