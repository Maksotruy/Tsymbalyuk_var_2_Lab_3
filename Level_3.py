def generate_subsets(symbols):
    n = len(symbols)

    for i in range(2 ** n):
        subset = []

        for j in range(n):
            if i & (1 << j):
                subset.append(symbols[j])

        print("{", ", ".join(subset), "}", sep="")


while True:
    text = input("Введіть символи без пробілів: ")

    if len(text) == 0:
        print("Помилка: рядок не може бути порожнім.")
        continue

    valid = True

    for i in range(len(text)):
        symbol = text[i]

        if not (
            "А" <= symbol <= "Я" or
            "а" <= symbol <= "я" or
            "A" <= symbol <= "Z" or
            "a" <= symbol <= "z" or
            symbol in "ІіЇїЄєҐґ"
        ):
            valid = False
            break

    if not valid:
        print("Помилка: можна вводити тільки літери без пробілів.")
        continue

    unique = True

    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if text[i] == text[j]:
                unique = False
                break

        if not unique:
            break

    if not unique:
        print("Помилка: символи не повинні повторюватися.")
        continue

    if len(text) > 10:
        print("Помилка: введіть не більше 10 символів.")
        continue

    break


print("Усі можливі підмножини:")
generate_subsets(text)

print("Кількість підмножин:", 2 ** len(text))