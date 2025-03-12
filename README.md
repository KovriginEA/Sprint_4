### Набор методов для работы со словарем books_genre и списком favorites:
***
## add_new_book
добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.

**Тест метода**

_test_add_new_book_add_two_books_
_test_add_new_book_two_same_books_
***
## set_book_genre
устанавливает жанр книги, если книга есть в books_genreи её жанр входит в списокgenre.

**Тест метода**

_test_set_book_genre_fantsctic_
_test_set_book_genre_dramma_is_not_allow_

***
## get_book_genre
выводит жанр книги по её имени.

**Тест метода**

_test_add_new_book_genry_is_empty_
_test_set_book_genre_dramma_is_not_allow_

***
## get_books_with_specific_genre
выводит список книг с определённым жанром.

**Тест метода**

_test_get_books_with_specific_genry_comedy_
***
## get_books_genre
выводит текущий словарь books_genre.

**Тест метода**

_test_get_books_with_specific_genry_comedy_

***
## get_books_for_children
возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.

**Тест метода**

_test_get_books_for_children_return_three_books_
***
## add_book_in_favorites
добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.

**Тест метода**

_test_add_book_in_favorites_add_book_
_test_add_book_in_favorites_twice_add_one_book_
_test_add_book_in_favorites_book_not_in_list_genre_notallowed_

***
## delete_book_from_favorites
удаляет книгу из избранного, если она там есть.

**Тест метода**

_test_delete_book_from_favorites_delete_is_succes_

***
## get_list_of_favorites_books
получает список избранных книг.

**Тест метода**

_test_delete_book_from_favorites_delete_is_succes_
_test_add_book_in_favorites_add_book_
_test_add_book_in_favorites_twice_add_one_book_
_test_add_book_in_favorites_book_not_in_list_genre_notallowed_