def reverse_number(number):
    reverse = 0

    for _ in str(number):
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10

    return reverse

def main():
    palindrome = []

    for x in range(100, 1000):
        for y in range(100, 1000):
            z = x * y
            if (z == reverse_number(z)):
                palindrome.append(z)

    palindrome.sort()
    print(palindrome)

if __name__ == "__main__":
    main()
