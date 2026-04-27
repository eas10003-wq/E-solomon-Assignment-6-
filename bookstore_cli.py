DB_NAME = "/Applications/bookstore.db"

import sqlite3

connection = sqlite3.connect("/Applications/bookstore.db")
cursor = connection.cursor()


def print_divider() -> None:
    print("\n" + "-" * 72)


def pause() -> None:
    input("\nPress Enter to continue...")


def print_menu() -> None:
    print_divider()
    print("Bookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. Count books per category")
    print("9. Search books by author")
    print("10. Quit")


def prompt_int(message: str) -> int:
    return int(input(message).strip())


def prompt_float(message: str) -> float:
    return float(input(message).strip())


def print_rows(headers, rows) -> None:
    if not rows:
        print("No results found.")
        return

    print(" | ".join(headers))
    print("-" * 72)
    for row in rows:
        print(" | ".join(str(value) for value in row))


def view_categories(cursor):
    cursor.execute("""
        SELECT categoryId, categoryName, categoryImage
        FROM category
        ORDER BY categoryId
    """)
    print_divider()
    print("Categories")
    print_rows(["ID", "Name", "Image"], cursor.fetchall())


def view_books(cursor):
    cursor.execute("""
        SELECT bookId, title, author, isbn, price, readNow
        FROM book
        ORDER BY title
    """)
    print_divider()
    print("Books")
    print_rows(["ID", "Title", "Author", "ISBN", "Price", "Read Now"], cursor.fetchall())


def view_books_in_category(cursor):
    category_id = prompt_int("Enter a category id: ")

    cursor.execute("""
        SELECT b.bookId, b.title, b.author, b.isbn, b.price, c.categoryName
        FROM book b
        JOIN category c ON b.categoryId = c.categoryId
        WHERE c.categoryId = ?
        ORDER BY b.title
    """, (category_id,))

    print_divider()
    print(f"Books in category {category_id}")
    print_rows(["ID", "Title", "Author", "ISBN", "Price", "Category"], cursor.fetchall())


def search_by_title(cursor):
    keyword = input("Enter a title keyword: ").strip()

    cursor.execute("""
        SELECT bookId, title, author, isbn, price
        FROM book
        WHERE title LIKE ?
        ORDER BY title
    """, (f"%{keyword}%",))

    print_divider()
    print(f"Books matching '{keyword}'")
    print_rows(["ID", "Title", "Author", "ISBN", "Price"], cursor.fetchall())


def search_by_author(cursor):
    keyword = input("Enter an author keyword: ").strip()

    cursor.execute("""
        SELECT bookId, title, author, price
        FROM book
        WHERE author LIKE ?
        ORDER BY author
    """, (f"%{keyword}%",))

    print_divider()
    print(f"Books by '{keyword}'")
    print_rows(["ID", "Title", "Author", "Price"], cursor.fetchall())


def add_book(connection):
    cursor = connection.cursor()

    try:
        category_id = prompt_int("Enter category id: ")
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = prompt_float("Enter price: ")
        image = input("Enter image filename: ").strip()
        read_now = prompt_int("Enter readNow (0 or 1): ")

        if read_now not in (0, 1):
            raise ValueError

        cursor.execute("""
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (category_id, title, author, isbn, price, image, read_now))

        connection.commit()

        print_divider()
        print("Book added successfully.")

    except ValueError:
        print_divider()
        print("Invalid input.")
    except sqlite3.IntegrityError as error:
        print_divider()
        print(f"Database error: {error}")


def update_book_price(connection):
    cursor = connection.cursor()

    try:
        book_id = prompt_int("Enter book id: ")
        new_price = prompt_float("Enter the new price: ")

        cursor.execute("""
            UPDATE book
            SET price = ?
            WHERE bookId = ?
        """, (new_price, book_id))

        connection.commit()

        print_divider()
        if cursor.rowcount == 0:
            print("No matching book was found.")
        else:
            print("Book price updated.")

    except ValueError:
        print_divider()
        print("Invalid input.")


def delete_book(connection):
    cursor = connection.cursor()

    try:
        book_id = prompt_int("Enter book id to delete: ")

        cursor.execute("""
            DELETE FROM book
            WHERE bookId = ?
        """, (book_id,))

        connection.commit()

        print_divider()
        if cursor.rowcount == 0:
            print("No matching book was found.")
        else:
            print("Book deleted.")

    except ValueError:
        print_divider()
        print("Invalid input.")


def count_books_per_category(cursor):
    cursor.execute("""
        SELECT c.categoryId, c.categoryName, COUNT(b.bookId)
        FROM category c
        LEFT JOIN book b ON c.categoryId = b.categoryId
        GROUP BY c.categoryId, c.categoryName
        ORDER BY c.categoryId
    """)

    print_divider()
    print("Books per category")
    print_rows(["ID", "Category", "Count"], cursor.fetchall())


def run_menu(connection):
    cursor = connection.cursor()

    while True:
        print_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            view_categories(cursor)
        elif choice == "2":
            view_books(cursor)
        elif choice == "3":
            view_books_in_category(cursor)
        elif choice == "4":
            search_by_title(cursor)
        elif choice == "5":
            add_book(connection)
        elif choice == "6":
            update_book_price(connection)
        elif choice == "7":
            delete_book(connection)
        elif choice == "8":
            count_books_per_category(cursor)
        elif choice == "9":
            search_by_author(cursor)
        elif choice == "10":
            print_divider()
            print("Goodbye!")
            break
        else:
            print_divider()
            print("Invalid option.")

        pause()


def main():
    print_divider()
    print("Welcome to the Bookstore CLI")

    with sqlite3.connect(DB_NAME) as connection:
        connection.execute("PRAGMA foreign_keys = ON;")
        run_menu(connection)

if __name__ == "__main__":
    main()

    import sqlite3

