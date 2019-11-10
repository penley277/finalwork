from models.ManagerFactory import ManagerFactory
from models.Book import Book
from list.BookList import BookList

if __name__ == '__main__':

    booklist = BookList()
    bookNo = "1111"
    bookName = "fdfdsf"
    author = "spl"
    bookCnt = 3
    borrowCnt = 1
    pubTime = "2019/10/13"
    book = Book(bookNo, bookName, author, bookCnt, borrowCnt, pubTime)

    bookNo = "111"
    bookName = "fdff"
    author = "spl"
    bookCnt = 2
    borrowCnt = 1
    pubTime = "2019/10/13"
    book2 = Book(bookNo, bookName, author, bookCnt, borrowCnt, pubTime)

    booklist.addBook(book)
    booklist.addBook(book2)
    booklist.outputBookList()

    stumanager = ManagerFactory.getManager(type="stu")
    print(stumanager.__class__)