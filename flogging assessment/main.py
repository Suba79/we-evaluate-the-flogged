password = input("Введите пароль: ")

SCORE = 0


def is_very_long(password):
    return len(password) >= 12


def found_digit(password):
    return any(char.isdigit() for char in password)


def has_upper_letters(password):
    return any(up_letters.isupper() for up_letters in password)


def has_lower_letters(password):
    return any(low_letters.islower() for low_letters in password)


def has_symbols(password):
    return any(not symbols.isalnum() for symbols in password)


checks = [
    is_very_long,
    found_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]

for check_func in checks:
    if check_func(password):
        SCORE += 2

print(f"Рейтинг пароля: {SCORE}")