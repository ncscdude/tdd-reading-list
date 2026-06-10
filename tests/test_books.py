from books import ReadingList


def test_new_reading_list_is_empty():
    reading_list = ReadingList()
    assert reading_list.get_all_books() == []


def test_can_add_a_book():
    reading_list = ReadingList()
    reading_list.add_book('The Hobbit')
    assert reading_list.get_all_books() == ['The Hobbit']


def test_can_add_multiple_books():
    reading_list = ReadingList()
    reading_list.add_book('The Hobbit')
    reading_list.add_book('Dune')
    assert reading_list.get_all_books() == ['The Hobbit', 'Dune']

