prime_file = open("primes.txt", "r")
primes = []
for line in prime_file.readlines():
    primes.append(int(line[:-1]))

def can_make_total(number):
    i = 0
    while primes[i] < number:
        p = primes[i]
        y = 1
        total = 0
        while total < number:
            total = p + 2 * y**2
            if total == number:
                return True
            elif total < number:
                y+=1
        i += 1
    return False


x = 21
found = True
while found:
    if x not in primes:
        found = can_make_total(x)
    x += 2

print(x)



