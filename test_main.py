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
    book_lst = ["Гарри Поттер и дары смерти", "Шерлок Холмс"]
    for book_name in book_lst:
        collector.add_new_book(book_name)
    return collector


# создаем фикстуру для создания экземпляра класса с коллекцией книг с присвоенными им жанрами
@pytest.fixture
def collector_with_books_and_genres():
    collector = BooksCollector()
    collection = [
        ["Гарри Поттер и дары смерти", "Фантастика"],
        ["Шерлок Холмс", "Детективы"],
        ["Том и Джерри", "Мультфильмы"],
        ["Достать ножи", "Детективы"],
        ["Друзья", "Комедии"],
    ]
    for book_name, genre in collection:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    return collector


# создаем фикстуру для создания экземпляра класса с коллекцией книг с присвоенными им жанрами, а также книгами в Избранном
@pytest.fixture
def collector_with_favorites(collector_with_books_and_genres):
    books_to_favorites = ["Гарри Поттер и дары смерти", "Том и Джерри"]
    for book in books_to_favorites:
        collector_with_books_and_genres.add_book_in_favorites(book)
    return collector_with_books_and_genres


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
        assert book_name in collector.books_genre.keys()

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
        assert book_name not in collector.books_genre.keys()

    # тестируем add_new_book - книга повторно не добавляется в коллекцию
    def test_add_new_book_add_added_book(self, collector):
        books_to_collection = ["Гарри Поттер и дары смерти", "Шерлок Холмс"]
        for book in books_to_collection:
            collector.add_new_book(book)
        before_adding_book_again = len(collector.books_genre)
        book_to_add_again = "Гарри Поттер и дары смерти"
        collector.add_new_book(book_to_add_again)
        after_adding_book_again = len(collector.books_genre)
        assert before_adding_book_again == after_adding_book_again

    # параметризация для проверки установки жанра у разных книг добавленных в books_genre
    @pytest.mark.parametrize(
        "book_name, genre",
        [["Гарри Поттер и дары смерти", "Фантастика"], ["Шерлок Холмс", "Детективы"]],
    )
    # тестируем set_book_genre - установка жанра соответсвенно книге у добавленных в books_genre книг
    def test_set_book_genre_books_from_books_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    # тестируем set_book_genre - книге не из books_genre жанр из genre не присваивается
    def test_set_book_genre_books_not_in_books_genre(self, collector):
        book_name = "Оно"
        genre = "Ужасы"
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.books_genre

    # тестируем set_book_genre - книге из books_genre не присваивается жанр не из genre
    def test_set_book_genre_genre_not_in_genre(self, collector):
        books_to_collection = ["Гарри Поттер и дары смерти", "Шерлок Холмс"]
        for book in books_to_collection:
            collector.add_new_book(book)
        book_name = "Гарри Поттер и дары смерти"
        genre = "Хоррор"
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre.get(book_name) == ""

    # параметризация для проверки соответствия выведенного жанра жанру в books_genre
    @pytest.mark.parametrize(
        "book_name, expected_genre",
        [
            ["Гарри Поттер и дары смерти", "Фантастика"],
            ["Шерлок Холмс", "Детективы"],
            ["Том и Джерри", "Мультфильмы"],
            ["Достать ножи", "Детективы"],
            ["Друзья", "Комедии"],
        ],
    )
    # тестируем get_book_genre - выводит присвоенный книге жанр по её имени
    def test_get_book_genre_book_with_genre_in_collection(
        self, collector, book_name, expected_genre
    ):
        books_with_genres = {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book_name) == expected_genre

    # тестируем get_book_genre - выводит пустое значение по имени книги, если жанр книге не был присвоен
    def test_get_book_genre_book_with_no_genre_in_collection(self, collector):
        books_to_collection = ["Гарри Поттер и дары смерти", "Шерлок Холмс"]
        for book in books_to_collection:
            collector.add_new_book(book)
        book_name = "Шерлок Холмс"
        assert collector.get_book_genre(book_name) == ""

    # тестируем get_books_with_specific_genre -  выводит список книг с жанром "Детективы" из списка genre
    def test_get_books_with_specific_genre_in_collection(self, collector):
        books_with_genres = {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        books_with_specific_genre = collector.get_books_with_specific_genre("Детективы")
        for book in books_with_specific_genre:
            assert collector.get_book_genre(book) == "Детективы"

    # параметризация для проверки вывода пустого списка, если жанра нет среди книг в коллекции и отсутствует в списке genre
    @pytest.mark.parametrize("unavailable_genre", ["Ужасы", "Хоррор"])
    # тестируем get_books_with_specific_genre -  выводит пустой список книг с жанром из списка genre,
    # так как книги с этим жанром не в коллекции, и с жанром "Хоррор", которого нет в  списке genre
    def test_get_books_with_specific_genre_empty_lst(
        self, collector, unavailable_genre
    ):
        books_with_genres = {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(unavailable_genre) == []

    # тестируем get_books_genre - получаем пустой словарь, если книги в коллекцию не были добавлены
    def test_get_books_genre_empty_collection(self, collector):
        assert collector.get_books_genre() == {}

    # тестируем get_books_genre - получаем словарь только с названиями книг, так как жанры не были присвоены
    def test_get_books_genre_collection_with_books(self, collector):
        books_to_collection = ["Гарри Поттер и дары смерти", "Шерлок Холмс"]
        for book in books_to_collection:
            collector.add_new_book(book)
        assert collector.get_books_genre() == {
            "Гарри Поттер и дары смерти": "",
            "Шерлок Холмс": "",
        }

    # тестируем get_books_genre - получаем словарь с названиями книг и присвоенными им жанрами
    def test_get_books_genre_collection_with_books_and_genres(self, collector):
        books_with_genres = {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_genre() == {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }

    # тестируем get_books_for_children - получаем книги подходящие детям с жанром не в genre_age_rating
    def test_get_books_for_children_genre_not_in_age_rating(self, collector):
        books_with_genres = {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        books_for_children = collector.get_books_for_children()
        for book in books_for_children:
            genre = collector.get_book_genre(book)
            assert genre not in collector.genre_age_rating

    # тестируем add_book_in_favorites - добавление новой книги из books_genre в favorites
    def test_add_book_in_favorites_book_from_books_genre(
        self, collector
    ):
        books_with_genres = {
            "Гарри Поттер и дары смерти": "Фантастика",
            "Шерлок Холмс": "Детективы",
            "Том и Джерри": "Мультфильмы",
            "Достать ножи": "Детективы",
            "Друзья": "Комедии",
        }
        for book, genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        book_name = "Достать ножи"
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    # параметризация для проверки, что книга не из не из books_genre и книга уже добавленная в favorites не могут быть добавлены в favorites
    @pytest.mark.parametrize(
        "unavailable_book_for_favorites", ["Гарри Поттер и дары смерти", "Оно"]
    )
    # тестируем add_book_in_favorites - книга не из books_genre и книга уже добавленная в favorites не могут быть добавлены в favorites
    def test_add_book_in_favorites_unavailable_books_for_favorites(
        self, collector_with_favorites, unavailable_book_for_favorites
    ):
        before_change_favorites = len(collector_with_favorites.favorites)
        collector_with_favorites.add_book_in_favorites(unavailable_book_for_favorites)
        after_change_favorites = len(collector_with_favorites.favorites)
        assert after_change_favorites == before_change_favorites

    # тестируем delete_book_from_favorites - книга, ранее добавленная в favorites, удаляется из favorites
    def test_delete_book_from_favorites_book_in_favorites(
        self, collector_with_favorites
    ):
        book_to_delete = "Том и Джерри"
        before_change_favorites = len(collector_with_favorites.favorites)
        collector_with_favorites.delete_book_from_favorites(book_to_delete)
        after_change_favorites = len(collector_with_favorites.favorites)
        assert book_to_delete not in collector_with_favorites.favorites
        assert book_to_delete in collector_with_favorites.books_genre
        assert after_change_favorites == before_change_favorites - 1

    # тестируем delete_book_from_favorites - книга не добавленная в favorites не может быть удалена из favorites
    def test_delete_book_from_favorites_book_not_in_favorites(
        self, collector_with_favorites
    ):
        book_to_delete = "Шерлок Холмс"
        before_change_favorites = len(collector_with_favorites.favorites)
        collector_with_favorites.delete_book_from_favorites(book_to_delete)
        after_change_favorites = len(collector_with_favorites.favorites)
        assert after_change_favorites == before_change_favorites

    # тестируем get_list_of_favorites_books - получение списка книг, добавленных в favorites
    def test_get_list_of_favorites_books_books_in_favorites(
        self, collector_with_favorites
    ):
        collector_with_favorites.get_list_of_favorites_books()
        assert collector_with_favorites.favorites == [
            "Гарри Поттер и дары смерти",
            "Том и Джерри",
        ]

    # тестируем get_list_of_favorites_books - получение пустого списка, если в favorites ничего не было добавлено
    def test_get_list_of_favorites_books_no_books_in_favorites(
        self, collector_with_books
    ):
        assert collector_with_books.get_list_of_favorites_books() == []
