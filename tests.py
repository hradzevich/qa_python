import pytest
from main import BooksCollector


# создаем фикстуру для создания экземпляра класса
@pytest.fixture
def collector():
    return BooksCollector()


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
        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # параметризация для проверки установки жанра у разных книг
    @pytest.mark.parametrize(
        "book_name, genre",
        [["Гарри Поттер", "Фантастика"], ["Шерлок Холмс", "Детективы"]],
    )
    # тестируем set_book_genre - установка жанра у добавленных в books_genre книг
    def test_set_book_genre_books_from_books_genre(
        self, collector, book_name, genre
    ):

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.books_genre[book_name] == genre
