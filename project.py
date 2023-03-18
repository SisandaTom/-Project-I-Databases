import sqlite3

# Create the database and table
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
             title TEXT,
             author TEXT,
             qty INTEGER)''')

# Insert initial data into the table
books = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
         (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
         (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
         (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
         (3005, 'Alice in Wonderland', 'Alice in Wonderland', 12)]
c.executemany('INSERT INTO books VALUES (?,?,?,?)', books)

# Define functions for adding, updating, deleting, and searching books
def add_book():
    id = input("Enter the book id: ")
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    qty = input("Enter the quantity of the book: ")
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    print("Book added successfully.")

def update_book():
    id = input("Enter the id of the book you want to update: ")
    field = input("Which field do you want to update (title, author, or qty): ")
    value = input("Enter the new value: ")
    c.execute(f"UPDATE books SET {field} = ? WHERE id = ?", (value, id))
    conn.commit()
    print("Book updated successfully.")

def delete_book():
    id = input("Enter the id of the book you want to delete: ")
    c.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    print("Book deleted successfully.")

def search_books():
    keyword = input("Enter a keyword to search for: ")
    c.execute("SELECT * FROM books WHERE id LIKE ? OR title LIKE ? OR author LIKE ?",
              (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
    results = c.fetchall()
    if results:
        print("Search results:")
        for row in results:
            print(row)
    else:
        print("No results found.")

# Define a main menu function
def main_menu():
    while True:
        print("\nWelcome to the ebookstore database!")
        print("Please choose an option:")
        print("1. Add a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Search for books")
        print("0. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")
# Run the main menu
main_menu()

# Close the database connection
conn.close()

