from app.accessors import BookAccessor


class BookService:
    @staticmethod
    def get_all_books():
        return BookAccessor.get_all_books()

    def get_single_book_by_id():
        pass