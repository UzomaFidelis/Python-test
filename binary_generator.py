import random


def binary_to_decimal(binary):
    """
    Takes a string representing a binary number
    and returns the decimal equivalent

    """
    binary = str(binary)

    agg = 0

    for index, digit in enumerate(binary[::-1]):
        agg += int(digit) * (2**index)

    return agg


def generate_binary_number():
    DIGITS = 4
    gen_number = ""

    for _ in range(DIGITS):
        gen_number += str(random.randint(0, 1))
    return gen_number


binary_number = generate_binary_number()
print("Binary Number: ", binary_number)

decimal_value = binary_to_decimal(binary_number)
print("Decimal Value: ", decimal_value)
