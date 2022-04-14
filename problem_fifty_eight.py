def read_primes():
    primes = []
    p = open("primes.txt", "r")
    s = p.readlines()
    for num in s:
        primes.append(int(num))
    return primes

def percent_primes(arr, primes):
    total_primes = [num for num in arr if num in primes]
    percent = len(total_primes) / (len(arr))
    return percent * 100

def add_layer(up, down, x):
    next = down[-1] + x
    up.append(next)
    next += x
    down.append(next)
    next += x
    up.append(next)
    next += x
    down.append(next)


primes = read_primes()
up = [3, 1, 7]
down = [5, 1, 9]
x = 4
while True:
    add_layer(up, down, x)
    arr = set(up + down)
    percent = percent_primes(arr, primes)
    #print(percent)
    if percent < 10:
        print(x + 1)
        break
    x += 2

print(x + 1)