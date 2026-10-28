def count_words(text):
    count = 0
    in_word = False

    for i in range(len(text)):
        if text[i] != " ":
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count


while True:
    text = input("Введіть рядок: ")

    if len(text) == 0:
        print("Помилка: рядок порожній.")
        continue

    has_letter = False
    invalid = False

    for i in range(len(text)):
        if ("а" <= text[i] <= "я" or
            "А" <= text[i] <= "Я" or
            "a" <= text[i] <= "z" or
            "A" <= text[i] <= "Z" or
            text[i] == "і" or text[i] == "І" or
            text[i] == "ї" or text[i] == "Ї" or
            text[i] == "є" or text[i] == "Є" or
            text[i] == "ґ" or text[i] == "Ґ"):

            has_letter = True

        elif text[i] == " ":
            continue

        else:
            invalid = True
            break

    if invalid:
        print("Помилка: дозволені тільки букви та пробіли.")
        continue

    if not has_letter:
        print("Помилка: потрібно ввести хоча б одне слово.")
        continue

    break


result = count_words(text)

print("Кількість слів:", result)