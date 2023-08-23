from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite with sqlite3 (books-collection.db)

# Creates a connection to a SQLite database.
# db = sqlite3.connect("books-collection.db")

# Creates a cursor to interact with the database.
# cursor = db.cursor()

# Creates a table called books with an id, title, author, and rating keys.
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# Creates data in the table.
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
# db.commit()

# SQLite with SQLAlchemy (instance/new-books-collection.db)

# Creates the extension.
db = SQLAlchemy()
# Configures the SQLite database relative to this file.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# Initializes the app with the extension.
db.init_app(app)

# Creates a table called Book with an id, title, author, and rating keys.
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# Creates a table schema in the database, and it requires the application context.
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Reads/returns all the rows in the table, and orders it by title.
    result = db.session.execute(db.select(Book).order_by(Book.title))
    # Uses .scalars() to get the elements from the rows.
    all_books = result.scalars()

    return render_template('index.html', books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Creates data in the table.
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # Updates one row by its id.
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()

        return redirect(url_for('home'))
    
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)

    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    # Deletes one row by its id.
    book_id = request.args.get('id')
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)