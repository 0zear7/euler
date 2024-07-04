# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


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
