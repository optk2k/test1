import re


def regexp_example(login):
    res = re.match(r"[a-z]", login[0])
    if res is None:
        return False, "первый символ не является латинским символом"
    res = re.match(r"^[a-z0-9\.-]+$", login)
    if res is None:
        return False, "логин должен состоять из латинских букв, цифр, точки и минуса"
    res = re.match(r"[a-z0-9]", login[-1])
    if res is None:
        return False, "последний символ логина должен быть латинской буквой или цифрой"
    length = len(login)
    if length > 20:
        return False, f"длина логина не должна быть больше 20 символов, сейчас {length}"

    return True, "логин прошел валидацию"


def regexp_example2(login):
    res = re.match(r"^([a-z]{1}|[a-z]{1}[a-z0-9\.-]{0,18}[a-z0-9]{1})$", login)
    if res is None:
        return False, "валидация не пройдена"
    else:
        return True, "валидация пройдена"


if __name__ == '__main__':
    "два варианта функции,"
    " первая может быть более гибкой и сообщать про ошибки на каждом шагу,"
    " втора короткая и менее информативная"
    print(regexp_example('.login'))
    print(regexp_example2('.login'))
