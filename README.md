# BooksCollector — приложение, которое позволяет установить жанр книги и добавить их в избранное

Это учебный проект Yandex.Practicum содержит автотесты на Python для класса **`BooksCollector`**, в котором реализовано добавление книг в коллекцию, присвоение им жанров, добавление в избранное и получение списка книг по определенному жанру и списка книг с рейтингом для детей.

## Реализованные тесты: 

### для метода add_new_book:
- Добавление новых книг в коллекцию и название книги содержит от 1 до 40 символов **test_add_new_book_add_books_with_valid_len**
- Проверка, что книга не может быть добавлена, если уже существует **test_add_new_book_add_added_book**
- Добавление книги с названием длиной менее 1 или более 40 символов **test_add_new_book_add_books_with_invalid_len**

### для метода set_book_genre:
- Присвоение жанра книге **test_set_book_genre_books_from_books_genre**
- Проверка, что жанр можно присвоить только книге из коллекции **test_set_book_genre_books_not_in_books_genre**
- Проверка, что жанр можно присвоить только из допустимого списка **test_set_book_genre_genre_not_in_genre**

### для метода get_book_genre:
- Получение жанра книги по ее названию **test_get_book_genre_book_with_genre_in_collection**
- Проверка, что если жанр книге не был присвоен, то при получении жанра по ее названию пустое значение 
**test_get_book_genre_book_with_no_genre_in_collection**

### для метода get_books_with_specific_genre:
- Получение списка книг определенного жанра **test_get_books_with_specific_genre_in_collection**
- Получение пустого списка, если жанра нет в списке жанров или среди присвоенных в коллекции **test_get_books_with_specific_genre_empty_lst**

### для метода get_books_genre:
- Получение  пустой коллекции **test_get_books_genre_empty_collection**
- Получение коллекции  без присвоенных жанров **test_get_books_genre_collection_with_books**
- Получение коллекции книг с присвоенными жанрами  **test_get_books_genre_collection_with_books_and_genres**

### для метода get_books_for_children:
- Получение списка книг, подходящих для детей **test_get_books_for_children_genre_not_in_age_rating**

### для метода add_book_in_favorites:
- Добавление книги в избранное **test_add_book_in_favorites_book_from_books_genre**
- Проверка, что нельзя добавить книгу в избранное дважды и нельзя добавить книгу, которой нет в коллекции **test_add_book_in_favorites_unavailable_books_for_favorites**

### для метода delete_book_from_favorites:
- Удаление книги из избранного **test_delete_book_from_favorites_book_in_favorites**
- Попытка удалить книгу, которой нет в избранном, не влияет на коллекцию  **test_delete_book_from_favorites_book_not_in_favorites**

### для метода get_list_of_favorites_books:
- Получение списка книг в избранном **test_get_list_of_favorites_books_books_in_favorites**
- Получение пустого списка, если нет книг в избранном  **test_get_list_of_favorites_books_no_books_in_favorites**
