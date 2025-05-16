class Book :
    total_books = 0

    def __init__(self,name):
        self.name = name
        self.increment_book_count()
        
    @classmethod
    def increment_book_count(cls) : 
        Book.total_books += 1
    
    @classmethod
    def dispay_books(cls) :
        print(f"Total books:",cls.total_books)


book1 = Book("eng")
Book.dispay_books()