def num_greater(p, q):
    return len(str(p)) > len(str(q))

p = 3
q = 2
total = 0
for x in range(999):
    if num_greater(p, q):
        total += 1
    old_p = p
    p = old_p + 2*q
    q = old_p + q
print(total)