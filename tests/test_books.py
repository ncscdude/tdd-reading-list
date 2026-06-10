from books import ReadingList


def test_new_reading_list_is_empty():
    reading_list = ReadingList()
    assert reading_list.get_all_books() == []


def test_can_add_a_book():
    reading_list = ReadingList()
    reading_list.add_book('The Hobbit')
    books = reading_list.get_all_books()
    assert books[0]['title'] == 'The Hobbit'


def test_can_add_multiple_books():
    reading_list = ReadingList()
    reading_list.add_book('The Hobbit')
    reading_list.add_book('Dune')
    books = reading_list.get_all_books()
    assert books[0]['title'] == 'The Hobbit'
    assert books[1]['title'] == 'Dune'


def test_new_book_is_unread_by_default():
    reading_list = ReadingList()
    reading_list.add_book('The Hobbit')
    books = reading_list.get_all_books()
    assert books[0]['read'] == False


def test_can_mark_book_as_read():
    reading_list = ReadingList()
    reading_list.add_book('The Hobbit')
    reading_list.mark_as_read('The Hobbit')
    books = reading_list.get_all_books()
    assert books[0]['read'] == True

