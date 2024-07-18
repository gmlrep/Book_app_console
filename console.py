from crud import CRUD

db = CRUD(json_file='database.json')


def find_all() -> dict:
    """
    Вывод всех книг из базы данных
    :return: Список книги в формате словаря
    """
    return db.find_all()


def create() -> None:
    """
    Добавление книги
    """
    print('Введите название книги')
    title = input()
    while title == '':
        print('Неверный тип данных')
        title = input()

    print('Введите автора книги')
    author = input()
    while author == '':
        print('Неверный тип данных')
        author = input()

    print('Введите год издания книги')
    year = input()
    while not year.isdigit() and year != '':
        print('Некорректный год')
        year = input()
    else:
        if year != '':
            while int(year) < 0 or int(year) > 2024:
                print('Некорректный год')
                year = input()
        else:
            pass

    db.create(title=title, author=author, year=int(year))


def find() -> list | None:
    """
    Поиск книги по фильтрам
    :return: Список книг
    """
    print('Введите название книги или нажмите enter, чтобы продолжить')
    title = input()

    print('Введите автора книги или нажмите enter, чтобы продолжить')
    author = input()

    print('Введите год издания книги или нажмите enter, чтобы продолжить')
    year = input()
    while not year.isdigit() and year != '':
        print('Некорректный год')
        year = input()
    else:
        if year != '':
            while int(year) < 0 or int(year) > 2024:
                print('Некорректный год')
                year = input()
        else:
            pass

    print('Введите статус книги или нажмите enter, чтобы продолжить')
    status = input()

    if year == '' and title == '' and author == '' and status == '':
        print("Данные для поиска не введены")

    result = db.read(title=title if title != '' else None,
                     author=author if author != '' else None,
                     status=status if status != '' else None,
                     year=int(year) if year != '' else None)
    return result


def delete() -> None:
    """
    Удаление книги по id
    """
    print("Введите ID книги, которую хотите удалить")
    book_id = input()
    while not book_id.isdigit():
        print("Некорректный ID")
        book_id = input()
    db.delete(book_id=int(book_id))


def update() -> None:
    """
    Изменение статуса книги по id
    """
    print('Введите ID книги')
    book_id = input()
    while not book_id.isdigit():
        print("Некорректный ID")
        book_id = input()
    print('Введите новый статус: "в наличии" или "выдана"')
    status = input()
    while status not in ['в наличии', 'выдана']:
        print("Неверный тип статуса")
        status = input()

    db.update(book_id=int(book_id), new_status=status)
