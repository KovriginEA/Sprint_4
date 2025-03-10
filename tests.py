import pytest

from main import BooksCollector

zomby_book = 'Гордость и предубеждение и зомби'
cat_killer_book = 'Что делать, если ваш кот хочет вас убить'

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book(cat_killer_book)
        assert len(collector.get_books_genre()) == 2

    #проверка добавления книг с одинаковыми названиями
    def test_add_new_book_two_same_books(self, collector):
        collector.add_new_book(zomby_book)
        assert len(collector.get_books_genre()) == 1

    #проверка что у добавленной книги пустой жанр
    def test_add_new_book_genry_is_empty(self, collector):
        assert collector.get_book_genre(zomby_book) == ''

    #проверка установления жанра книги фантастика
    def test_set_book_genre_fantsctic(self, collector):
        collector.set_book_genre(zomby_book,collector.genre[0])
        assert collector.get_book_genre(zomby_book) == collector.genre[0]

    #проверка получения жанра книги
    @pytest.mark.parametrize('allowed_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_book_genry_there_genry_from_allowed_list(self, allowed_genre):
        collector = BooksCollector()
        collector.books_genre[zomby_book] = allowed_genre
        assert collector.get_book_genre(zomby_book) == allowed_genre


    #проверка что нельзя поставить недопустимый жанр
    @pytest.mark.parametrize('my_genre',['Биография', 'Раскраска', 'Исторический'])
    def test_set_book_genre_there_genre_not_in_list_is_not_allow(self, collector, my_genre):
        collector.set_book_genre(zomby_book, my_genre)
        assert collector.get_book_genre(zomby_book) == ''

    #проверка получения книг с жанром Комедии
    def test_get_books_with_specific_genry_comedy(self, collector):
        collector.set_book_genre(zomby_book, 'Комедии')
        collector.add_new_book(cat_killer_book)
        collector.set_book_genre(cat_killer_book, 'Ужасы')
        collector.add_new_book('Жизненно важный вопрос')
        collector.set_book_genre('Жизненно важный вопрос', 'Детективы')
        assert collector.get_books_with_specific_genre('Комедии') == [zomby_book]

    #проверка получения книг для детей
    def test_get_books_for_children_return_three_books(self, collector):
        collector.set_book_genre(zomby_book, collector.genre[0])
        collector.add_new_book(cat_killer_book)
        collector.set_book_genre(cat_killer_book, collector.genre[1])
        collector.add_new_book('Жизненно важный вопрос')
        collector.set_book_genre('Жизненно важный вопрос', collector.genre[2])
        collector.add_new_book('Дорога в будущее')
        collector.set_book_genre('Дорога в будущее', collector.genre[3])
        collector.add_new_book('Ход царем')
        collector.set_book_genre('Ход царем', collector.genre[4])
        assert len(collector.get_books_for_children()) == 3

    #проверка добавления одной книги в избранное из списка book_genre
    def test_add_book_in_favorites_add_one_book_succesfuly(self, collector):
        collector.add_book_in_favorites(zomby_book)
        assert collector.get_list_of_favorites_books() == [zomby_book]

    #проверка что одну книгу нельзя повторно добавить в избранное
    def test_add_book_in_favorites_twice_add_one_book(self, collector):
        collector.add_book_in_favorites(zomby_book)
        collector.add_book_in_favorites(zomby_book)
        assert len(collector.get_list_of_favorites_books()) == 1

    #проверка что нельзя добавлять книгу в избранное не из списка books_genre
    @pytest.mark.parametrize('book_not_in_genre', ['MMA for dog', 'I love winter', 'Corban Dallas'])
    def test_add_book_in_favorites_book_not_in_list_genre_notallowed(self, book_not_in_genre)  :
        collector = BooksCollector()
        collector.add_book_in_favorites(book_not_in_genre)
        assert len(collector.get_list_of_favorites_books()) == 0

    #проверка удаления книги из избранного
    def test_delete_book_from_favorites_delete_is_succes(self, collector):
        collector.add_book_in_favorites(zomby_book)
        collector.delete_book_from_favorites(zomby_book)
        assert collector.get_list_of_favorites_books() == []
