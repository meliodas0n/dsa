import math


def one(n):
    num = n
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return f"Number of digits in {num} : {count}"


def two(n):
    return f"Number of digits in {n} : {len(str(n))}"


def three(n):
    return f"Number of digits in {n} : {math.floor(math.log10(n) + 1)}"


if __name__ == "__main__":
    n = int(input("What is the number ; "))
    print(one(n))
    print(two(n))
    print(three(n))
