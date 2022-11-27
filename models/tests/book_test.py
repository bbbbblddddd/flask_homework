import unittest

from book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('Frankenstein', 'Mary Shelley', 'Horror', "Mary Shelley's chilling Gothic tale was conceived when she was only eighteen, living with her lover Percy Shelley on Lake Geneva. The story of Victor Frankenstein who, obsessed with creating life itself, plunders graveyards for the material to fashion a new being, but whose botched creature sets out to destroy his maker, would become the world's most famous work of horror fiction, and remains a devastating exploration of the limits of human creativity. Based on the third edition of 1831, this volume contains all Mary Shelley's revisions to her story, and also includes 'A Fragment' by Lord Byron and Dr John Polidori's 'The Vampyre: A Tale'.", True)

    def book_has_a_title(self):
        self.assertEqual('Frankenstein', self.book.title)

if __name__ == "__main__":
    unittest.main()