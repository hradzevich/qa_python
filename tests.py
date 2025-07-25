import pytest
from main import BooksCollector


# создаем фикстуру для создания экземпляра класса
@pytest.fixture
def collector():
    return BooksCollector()


# создаем фикстуру для создания экземпляра класса с коллекцией книг без присвоенных жанров
@pytest.fixture
def collector_with_books():
    collector = BooksCollector()
    book_lst = ["Гарри Поттер", "Шерлок Холмс"]
    for book_name in book_lst:
        collector.add_new_book(book_name)
    return collector


# создаем фикстуру для создания экземпляра класса с коллекцией книг с присвоенными им жанрами
@pytest.fixture
def collector_with_books_and_genres():
    collector = BooksCollector()
    collection = [
        ["Гарри Поттер", "Фантастика"],
        ["Шерлок Холмс", "Детективы"],
        ["Том и Джерри", "Мультфильмы"],
        ["Друзья", "Комедии"],
    ]
    for book_name, genre in collection:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:
    # тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    # параметризация для проверки установки жанра у разных книг добавленных в books_genre
    @pytest.mark.parametrize("genre", ["Фантастика", "Детективы"])
    # тестируем set_book_genre - установка жанра соответсвенно книге у добавленных в books_genre книг
    def test_set_book_genre_books_from_books_genre(self, collector_with_books, genre):
        for book in collector_with_books.books_genre.keys():
            collector_with_books.set_book_genre(book, genre)
            assert collector_with_books.books_genre[book] == genre

    # тестируем set_book_genre - книге не из books_genre жанр из genre не присваивается
    def test_set_book_genre_books_not_in_books_genre(
        self, collector_with_books):
        book_name = "Оно"
        genre = "Ужасы"
        collector_with_books.set_book_genre(book_name, genre)
        assert book_name not in collector_with_books_and_genres.books_genre

    # тестируем set_book_genre - книге из books_genre не присваивается жанр не из genre
    def test_set_book_genre_genre_not_in_genre(self, collector_with_books):
        book_name = "Гарри Поттер"
        genre = "Хоррор"
        collector_with_books.set_book_genre(book_name, genre)
        assert collector_with_books.books_genre.get(book_name) == ""
