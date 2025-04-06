from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# App
app = Flask(__name__)
app.secret_key = "some secret string"

# Form
class MyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
    submit = SubmitField(label="Add Book")

class RatingForm(FlaskForm):
    rating = IntegerField('rating', validators=[DataRequired()])
    submit = SubmitField(label="Edit Rating")

# DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# Bootstrap
bootstrap = Bootstrap5(app)



@app.route('/')
def index():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["Post", "Get"])
def add():
    form = MyForm()
    if form.validate_on_submit():
        with app.app_context():
            new_book = Book(
                title=request.form['title'], 
                author=request.form['author'], 
                rating=request.form['rating']
                )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html", form=form)

@app.route('/edit', methods=["Post", "Get"])
def edit():
    form = RatingForm()
    bookId = request.args.get('bookId')
    print(bookId)
    if form.validate_on_submit():
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == bookId)).scalar()
            book_to_update.rating = request.form['rating']
            db.session.commit() 
        return redirect(url_for('index'))
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == bookId)).scalar()
    return render_template("edit.html", book=book, form=form)

@app.route("/delete")
def delete():
    book_id = request.args.get('bookId')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

