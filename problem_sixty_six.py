import math
def is_square(x):
    root = math.sqrt(x)
    return int(root + 0.5) **2 == x

def get_continued_fractions(n):
    ai = 0
    val = 0
    remainder = 0
    repeating_list = []

    remainder = 1.0/math.sqrt(n)
    index = 0
    while True:
        val = 1.0/remainder
        ai = int(val)
        remainder = val-ai
        repeating_list.append(ai)
        if repeating_list[index] == 2 * repeating_list[0]:
            break
        index += 1
    return repeating_list

largest = 0
for D in range(2, 1001):
    if not is_square(D):
        a_values = get_continued_fractions(D)
        current_index = 0
        a = a_values[0]
        repeats = a_values[1:]
        h_minus_2 = 0
        h_minus_1 = 1
        k_minus_2 = 1
        k_minus_1 = 0

        while True:
            h = a*h_minus_1 + h_minus_2
            k = a*k_minus_1 + k_minus_2

            if (h*h) - D * (k*k) == 1:
                if h > largest:
                    largest = h
                    print("Largest D: " + str(D))
                break
            else:
                k_minus_2 = k_minus_1
                h_minus_2 = h_minus_1
                h_minus_1 = h
                k_minus_1 = k
                a = repeats[current_index % len(repeats)]
                current_index += 1

print(largest)








