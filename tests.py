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
    book_lst = ["Гарри Поттер и дары смерти", "Шерлок Холмс. Пустой дом"]
    for book_name in book_lst:
        collector.add_new_book(book_name)
    return collector


# создаем фикстуру для создания экземпляра класса с коллекцией книг с присвоенными им жанрами
@pytest.fixture
def collector_with_books_and_genres():
    collector = BooksCollector()
    collection = [
        ["Гарри Поттер и дары смерти", "Фантастика"],
        ["Шерлок Холмс. Пустой дом", "Детективы"],
        ["Том и Джерри", "Мультфильмы"],
        ["Друзья", "Комедии"],
    ]
    for book_name, genre in collection:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
class TestBooksCollector:
    # параметризация для проверки добавления книг с валидным количеством символов в названии (1, 2, 39, 40)
    @pytest.mark.parametrize(
        "book_name",
        [
            "Я",
            "Мы",
            "Тайны затерянного города среди джунглей",
            "Тени исчезают в тумане над старым мостом",
        ],
    )
    # тестируем add_new_book - добавление книг с валидным количеством символов в названии
    def test_add_new_book_add_books_with_valid_len(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 4

    # параметризация для проверки, что книги с невалидным количеством символов в названии (0, 41, 59) не попадают в коллекцию
    @pytest.mark.parametrize(
        "book_name",
        [
            "",
            "Проклятие заброшенного дома на краю света",
            "Тайны древних руин, скрывающихся под покровом ночи и тумана",
        ],
    )
    # тестируем add_new_book - книги с невалидным количеством символов в названии не добавляются в коллекцию
    def test_add_new_book_add_books_with_invalid_len(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    # тестируем add_new_book - книга повторно не добавляется в коллекцию
    def test_add_new_book_add_added_book(self, collector_with_books_and_genres):
        book_name = "Гарри Поттер и дары смерти"
        before_adding_book_again = len(collector_with_books_and_genres.books_genre)
        collector_with_books_and_genres.add_new_book(book_name)
        after_adding_book_again = len(collector_with_books_and_genres.books_genre)
        assert (
            before_adding_book_again == after_adding_book_again
            and collector_with_books_and_genres.get_book_genre(book_name)
            == "Фантастика"
        )

    # параметризация для проверки установки жанра у разных книг добавленных в books_genre
    @pytest.mark.parametrize("genre", ["Фантастика", "Детективы"])
    # тестируем set_book_genre - установка жанра соответсвенно книге у добавленных в books_genre книг
    def test_set_book_genre_books_from_books_genre(self, collector_with_books, genre):
        for book in collector_with_books.books_genre.keys():
            collector_with_books.set_book_genre(book, genre)
            assert collector_with_books.books_genre[book] == genre

    # тестируем set_book_genre - книге не из books_genre жанр из genre не присваивается
    def test_set_book_genre_books_not_in_books_genre(self, collector_with_books):
        book_name = "Оно"
        genre = "Ужасы"
        collector_with_books.set_book_genre(book_name, genre)
        assert book_name not in collector_with_books.books_genre

    # тестируем set_book_genre - книге из books_genre не присваивается жанр не из genre
    def test_set_book_genre_genre_not_in_genre(self, collector_with_books):
        book_name = "Гарри Поттер"
        genre = "Хоррор"
        collector_with_books.set_book_genre(book_name, genre)
        assert collector_with_books.books_genre.get(book_name) == ""

    # параметризация для проверки соответствия выведенного жанра жанру в books_genre
    @pytest.mark.parametrize("book_name, expected_genre",
    [
        ["Гарри Поттер и дары смерти", "Фантастика"],
        ["Шерлок Холмс. Пустой дом", "Детективы"],
        ["Том и Джерри", "Мультфильмы"],
        ["Друзья", "Комедии"],
    ])
    # тестируем get_book_genre - выводит присвоенный книге жанр по её имени
    def test_get_book_genre_book_with_genre_in_collection(self, collector_with_books_and_genres, book_name, expected_genre):
        genre_in_collection = collector_with_books_and_genres.get_book_genre(book_name)
        assert genre_in_collection == expected_genre
    
    # тестируем get_book_genre - выводит пустое значение по имени книги, если жанр книге не был присвоен
    def test_get_book_genre_book_with_genre_in_collection(self, collector_with_books):
        book_name = "Шерлок Холмс. Пустой дом"
        assert collector_with_books.get_book_genre(book_name) == ""

      