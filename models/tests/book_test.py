import unittest

from book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('Frankenstein', 'Mary Shelley', 'Horror', "Mary Shelley's chilling Gothic tale was conceived when she was only eighteen, living with her lover Percy Shelley on Lake Geneva. The story of Victor Frankenstein who, obsessed with creating life itself, plunders graveyards for the material to fashion a new being, but whose botched creature sets out to destroy his maker, would become the world's most famous work of horror fiction, and remains a devastating exploration of the limits of human creativity. Based on the third edition of 1831, this volume contains all Mary Shelley's revisions to her story, and also includes 'A Fragment' by Lord Byron and Dr John Polidori's 'The Vampyre: A Tale'.", True)

    def test_book_has_a_title(self):
        self.assertEqual('Frankenstein', self.book.title)

    def test_book_has_author(self):
        self.assertEqual('Mary Shelley', self.book.author)

    def test_book_has_genre(self):
        self.assertEqual('Horror', self.book.genre)

    def test_book_has_description(self):
        self.assertEqual("Mary Shelley's chilling Gothic tale was conceived when she was only eighteen, living with her lover Percy Shelley on Lake Geneva. The story of Victor Frankenstein who, obsessed with creating life itself, plunders graveyards for the material to fashion a new being, but whose botched creature sets out to destroy his maker, would become the world's most famous work of horror fiction, and remains a devastating exploration of the limits of human creativity. Based on the third edition of 1831, this volume contains all Mary Shelley's revisions to her story, and also includes 'A Fragment' by Lord Byron and Dr John Polidori's 'The Vampyre: A Tale'.", self.book.description)

    def test_book_shows_checked_out_status(self):
        self.assertEqual(True, self.book.checked_out)

    # def test_book_can_be_added(self):
    #     book = Book('Frankenstein', 'Mary Shelley', 'Horror', "Mary Shelley's chilling Gothic tale was conceived when she was only eighteen, living with her lover Percy Shelley on Lake Geneva. The story of Victor Frankenstein who, obsessed with creating life itself, plunders graveyards for the material to fashion a new being, but whose botched creature sets out to destroy his maker, would become the world's most famous work of horror fiction, and remains a devastating exploration of the limits of human creativity. Based on the third edition of 1831, this volume contains all Mary Shelley's revisions to her story, and also includes 'A Fragment' by Lord Byron and Dr John Polidori's 'The Vampyre: A Tale'.", True)
    #     self.book.add_book(book)

    



if __name__ == "__main__":
    unittest.main()

