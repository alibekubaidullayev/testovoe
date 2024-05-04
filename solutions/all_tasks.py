def task_1(number):
    last_digit = number % 10
    if last_digit == 0 or last_digit in range(5, 10) or number in range(11, 15):
        return f"{number} компьютеров"
    elif last_digit in range(2, 5):
        return f"{number} компьютера"
    else:
        return f"{number} компьютер"


def task_2(arr):
    minimal = min(arr)
    dividers = []

    limit = int(minimal * 0.5)

    for i in range(2, limit + 1):
        if minimal % i == 0:
            flag = True
            for x in arr:
                if x % i != 0:
                    flag = False
                    break

            if flag:
                dividers.append(i)

    return dividers


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def task_3(n, m):
    res = []

    for x in range(n, m + 1):
        if isPrime(x):
            res.append(x)

    return res


def task_4(n):
    print(f"{'':>3}", end="")
    for j in range(1, n + 1):
        print(f"{j:>3}", end="")
    print()

    for i in range(1, n + 1):
        print(f"{i:>3}", end="")
        for j in range(1, n + 1):
            print(f"{i * j:>3}", end="")
        print()


if __name__ == "__main__":
    print(task_1(25))
    print(task_1(41))
    print(task_1(1048))
    print(task_2([42, 12, 18]))
    print(task_3(11, 20))
    task_4(5)
