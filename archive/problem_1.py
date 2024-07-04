x = [3, 5]
multiples = []

for i in x:
    y = 1
    while i * y < 1000:
        if (i * y < 1000):
            multiples.append(i * y)
        y += 1

sum = 0

for i in list(set(multiples)):
    sum += i

print(sum)
