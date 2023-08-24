from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
import requests
from movie_form import RateMovieForm

app = Flask(__name__)
app.secret_key = "Luke, I am your father"
Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies-collection.db"
db.init_app(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars()

    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        new_movie = Movie(
            title=request.form["title"],
            year=request.form["year"],
            description=request.form["description"],
            rating=request.form["rating"],
            ranking=request.form["ranking"],
            review=request.form["review"],
            img_url=request.form["img_url"],
        )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for("home"))
    
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True, port=5004)
