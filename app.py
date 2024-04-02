# importing Models
from src.Models.Catalog import Catalog
from src.Models.Book import Book
from src.Models.Magazine import Magazine
from src.Models.CD import CD
from src.Models.Item import Item

# importing User Models
from src.Models.Users.Librarian import Librarian
from src.Models.Users.Patron import Patron

# importing Controllers
from src.Controllers.LibrarySystem import LibrarySystem


def main():
    catalog = Catalog()
    library_system = LibrarySystem(catalog)
    _user = Librarian("John Doe", 1)
    # Depending on a user state, the user can be a Librarian or a Patron
    if isinstance(_user, Librarian):
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

    elif isinstance(_user, Patron):
        while True:
            print("1. Check Out Item\n2. Check In Item\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                item_id = input("Enter the ID of the item you want to check out: ")
                library_system.check_out_item(item_id)
            elif choice == '2':
                item_id = input("Enter the ID of the item you want to check in: ")
                library_system.check_in_item(item_id)
            elif choice == '3':
                break
            else:
                print("Invalid option.")


if __name__ == "__main__":
    main()
