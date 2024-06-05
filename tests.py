import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_initialization_all_genres_exists(self):
        collector = BooksCollector()

        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_when_book_already_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book_name', ['', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя12345678'])
    def test_add_new_book_with_invalid_name(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_valid_genre(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Any book')
        collector.set_book_genre('Any book', genre)

        assert collector.get_book_genre('Any book') == genre

    def test_set_book_genre_when_book_not_exists(self):
        collector = BooksCollector()

        book_name = 'Шерлок Холмс'
        genre = 'Детективы'
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == None

    def test_set_book_genre_when_genre_not_exists(self):
        collector = BooksCollector()

        book_name = 'Гарри Поттер'
        genre = 'Фэнтези'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == ''

    def test_get_book_genre_when_book_and_genre_exists(self):
        collector = BooksCollector()

        collector.add_new_book('Питер Пэн')
        collector.set_book_genre('Питер Пэн', 'Мультфильмы')

        assert collector.get_book_genre('Питер Пэн') == 'Мультфильмы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Питер Пэн')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Питер Пэн', 'Мультфильмы')

        specific_genre_books = collector.get_books_with_specific_genre('Фантастика')
        assert specific_genre_books == ['Властелин колец', 'Гарри Поттер']

    def test_get_books_genre_with_multiple_books(self):
        collector = BooksCollector()

        expected_books = {
            'Властелин колец': 'Фантастика',
            'Гарри Поттер': 'Фантастика',
            'Питер Пэн': 'Мультфильмы'
        }

        for book, genre in expected_books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        actual_books = collector.get_books_genre()
        assert actual_books == expected_books

    def test_get_books_for_children_get_two_books(self):
        collector = BooksCollector()

        books_for_children = {
            'Гарри Поттер': 'Фантастика',
            'Питер Пэн': 'Мультфильмы'
        }
        books_for_adults = {
            '1408': 'Ужасы'
        }
        books = {**books_for_children, **books_for_adults}

        for book, genre in books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        actual_books_for_children = collector.get_books_for_children()
        assert sorted(actual_books_for_children) == sorted(books_for_children.keys())

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('1408')
        collector.add_book_in_favorites('1408')
        collector.delete_book_from_favorites('1408')

        assert '1408' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_list_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Властелин колец')
        books = collector.get_list_of_favorites_books()

        assert books == ['Гарри Поттер', 'Властелин колец']






















