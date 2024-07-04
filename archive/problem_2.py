sequence = [1, 2]

while sequence[-2] + sequence[-1] < 4000000:
    sequence.append(sequence[-2] + sequence[-1])

sum = 0

for i in sequence:
    if (i % 2 == 0):
        sum += i
