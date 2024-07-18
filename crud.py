import json
from json import JSONDecodeError


class CRUD:

    def __init__(self, json_file):
        self.data = json_file

    def create(self, title: str,
               author: str,
               year: int) -> None:
        """
        Добавление книги в базу данных
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        """
        with open(self.data, 'r', encoding='utf-8') as file_r:
            try:
                data = json.load(file_r)
                list_id = [int(id_b) for id_b in data]
                book_id = max(list_id) + 1
            except JSONDecodeError:
                data = {}
                book_id = 1

        data[f'{book_id}'] = {'title': title, 'author': author, 'year': year, 'status': 'в наличии'}

        with open(self.data, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    def read(self, title: str | None = None,
             author: str | None = None,
             year: int | None = None,
             status: str | None = None) -> list | None:
        """
        Вывод книги по фильтрам
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        :param status: Статус книги
        :return: Список книги, удовлетворяющие условиям
        """
        result_search = []
        with open(self.data, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                return
        for book in data:
            if (book not in result_search and
                    (((title is not None and data[book]['title'] == title) or title is None) and
                     ((author is not None and data[book]['author'] == author) or author is None) and
                     ((year is not None and data[book]['year'] == year) or year is None) and
                     ((status is not None and data[book]['status'] == status) or status is None))):
                result_search.append({book: data[book]})
        return result_search

    def find_all(self) -> dict | None:
        """
        Вывод всех книг из базы данных
        :return: Словарь из всех книг
        """
        with open(self.data, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                print("База данных пуста")
                return
        return data

    def update(self, book_id: int,
               new_status: str):
        """
        Изменения статуса книги
        :param book_id: Уникальный ID книги
        :param new_status: Новый статус для обновления
        """
        if new_status not in ['в наличии', 'выдана']:
            print("Неверный тип статуса")
            return

        with open(self.data, 'r', encoding='utf-8') as file_r:
            data = json.load(file_r)
        try:
            data[f'{book_id}']['status'] = new_status
        except KeyError:
            print('Книги с таким ID не существует')
            return
        with open(self.data, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    def delete(self, book_id: int):
        """
        Удаление книги
        :param book_id: Уникальный ID книги
        """
        with open(self.data, 'r', encoding='utf-8') as file_r:
            data = json.load(file_r)
        try:
            del data[f'{book_id}']
        except KeyError:
            print('Книги с таким ID не существует')
            return
        with open(self.data, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
