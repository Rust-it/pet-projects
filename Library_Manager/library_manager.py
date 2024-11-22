import json
import uuid
from typing import List, Dict, Any

class Library:
    """Управляет данными библиотеки."""

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> List["Book"]:
        """Загружает книги из файла."""
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Book(**book_data) for book_data in data]
        except FileNotFoundError:
            return []

    def save_books(self):
        """Сохраняет книги в файл."""
        with open(self.filename, "w") as f:
            json.dump([vars(book) for book in self.books], f, indent=4)

    def add_book(self):
        """Добавляет книгу в библиотеку."""
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        while True:
            try:
                year = int(input("Введите год издания: "))
                break
            except ValueError:
                print("Некорректный год. Попробуйте еще раз.")
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()
        print("Книга добавлена.")

    def delete_book(self):
        """Удаляет книгу из библиотеки."""
        book_id = input("Введите ID книги для удаления: ")
        try:
            self.books = [book for book in self.books if book.id != book_id]
            self.save_books()
            print("Книга удалена.")
        except ValueError:
            print("Книга с таким ID не найдена.")

    def search_book(self):
        """Ищет книги по названию, автору или году."""
        search_term = input("Введите название, автора или год для поиска: ")
        results = [book for book in self.books if search_term.lower() in book.title.lower() or \
                   search_term.lower() in book.author.lower() or \
                   search_term in str(book.year)]
        if results:
            print("Найденные книги:")
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")

    def display_all_books(self):
        """Отображает все книги в библиотеке."""
        if self.books:
            print("Список всех книг:")
            for book in self.books:
                print(book)
        else:
            print("Библиотека пуста.")

    def change_book_status(self):
        """Меняет статус книги."""
        book_id = input("Введите ID книги для изменения статуса: ")
        new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").lower()
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_books()
                    print("Статус книги изменен.")
                    return
                else:
                    print("Некорректный статус.")
                    return
        print("Книга с таким ID не найдена.")


class Book:
    """Представляет книгу."""

    def __init__(self, title: str, author: str, year: int, book_id: str = None, status: str = "в наличии"):
        self.id: str = book_id or str(uuid.uuid4())
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    def __str__(self):
        return f"ID: {self.id}\nНазвание: {self.title}\nАвтор: {self.author}\nГод: {self.year}\nСтатус: {self.status}\n{'*' * 20}"


def main():
    """Главная функция приложения."""
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.delete_book()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.display_all_books()
        elif choice == "5":
            library.change_book_status()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()