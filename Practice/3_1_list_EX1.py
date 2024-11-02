NUMBERS = [1, -2, 3, -4, 5, -6, 7, -8]

POSITIVE_NUMBER = [num for num in NUMBERS if num >= 0]
NEGATIVE_NUMBER = [num for num in NUMBERS if num < 0]
EVEN_NUMBER = [num for num in NUMBERS if num % 2 == 0]
ODD_NUMBER = [num for num in NUMBERS if num % 2 != 0]

print(ODD_NUMBER)