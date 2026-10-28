def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    try:
        n = int(input("Введіть номер числа Фібоначчі: "))

        if n < 0:
            print("Помилка: число не може бути від'ємним.")
            continue

        if n > 35:
            print("Помилка: введіть число не більше 35.")
            continue

        break

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


result = fibonacci(n)

print("Число Фібоначчі:", result)