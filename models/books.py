from models.book import Book

book1 = Book('Frankenstein', 'Mary Shelley', 'Horror', "Mary Shelley's chilling Gothic tale was conceived when she was only eighteen, living with her lover Percy Shelley on Lake Geneva. The story of Victor Frankenstein who, obsessed with creating life itself, plunders graveyards for the material to fashion a new being, but whose botched creature sets out to destroy his maker, would become the world's most famous work of horror fiction, and remains a devastating exploration of the limits of human creativity. Based on the third edition of 1831, this volume contains all Mary Shelley's revisions to her story, and also includes 'A Fragment' by Lord Byron and Dr John Polidori's 'The Vampyre: A Tale'.", True)
book2 = Book('The Outsider', 'Albert Camus', 'Drama', "In The Outsider, his classic existentialist novel, Camus explores the alienation of an individual who refuses to conform to social norms. Meursault, his anti-hero, will not lie. When his mother dies, he refuses to show his emotions simply to satisfy the expectations of others. And when he commits a random act of violence on a sun-drenched beach near Algiers, his lack of remorse compounds his guilt in the eyes of society and the law. Yet he is as much a victim as a criminal.", False)
book3 = Book('1984', 'George Orwell', 'Sci-Fi', "Winston Smith works for the Ministry of Truth in London, chief city of Airstrip One. Big Brother stares out from every poster, the Thought Police uncover every act of betrayal. When Winston finds love with Julia, he discovers that life does not have to be dull and deadening, and awakens to new possibilities. Despite the police helicopters that hover and circle overhead, Winston and Julia begin to question the Party; they are drawn towards conspiracy. Yet Big Brother will not tolerate dissent - even in the mind. For those with original thoughts they invented Room 101. . .", False)

books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def delete_book(title):
    book_to_delete = None
    for book in books:
        if book.title == title:
            book_to_delete = book
            break

    books.remove(book_to_delete)

