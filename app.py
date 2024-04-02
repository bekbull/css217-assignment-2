# importing Models
from src.Models.Catalog import Catalog
from src.Models.Book import Book
from src.Models.Magazine import Magazine
from src.Models.CD import CD
from src.Models.Item import Item

# importing Controllers
from src.Controllers.LibrarySystem import LibrarySystem


def main():
    catalog = Catalog()
    library_system = LibrarySystem(catalog)

    while True:
        print("1. Add Book\n2. Add Magazine\n3. Add CD\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            item_id = input("ID: ")
            isbn = input("ISBN: ")
            genre = input("Genre: ")
            library_system.add_item(Book, title, author, item_id, isbn, genre)
            print("Book added.")
        elif choice == '2':
            title = input("Title: ")
            author = input("Author: ")
            item_id = input("ID: ")
            issue = input("Issue: ")
            library_system.add_item(Magazine, title, author, item_id, issue)
            print("Magazine added.")
        elif choice == '3':
            title = input("Title: ")
            author = input("Author: ")
            item_id = input("ID: ")
            duration = input("Duration: ")
            library_system.add_item(CD, title, author, item_id, duration)
            print("CD added.")
        elif choice == '4':
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
