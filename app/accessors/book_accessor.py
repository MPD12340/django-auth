from app.models import Book


class BookAccessor:
    """book accessor to handle the database logic"""
    
    @staticmethod
    def get_all_books():
        return Book.objects.all()

    # @staticmethod
    # def get_books_of_a_author(author_id):
