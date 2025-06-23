import os
import requests
import data_fetch
from flask import Flask, render_template, request, redirect, url_for, flash
from data_manager import DataManager
from models import db, Movie, User

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{basedir}/data/movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key-here'

db.init_app(app)
data_manager = DataManager()

@app.route('/')
def home():
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    name = request.form.get('name')
    if name and name.strip():
        data_manager.create_user(name=name.strip())
        flash('User added successfully!', 'success')
    else:
        flash('Username cannot be empty!', 'error')
    return redirect(url_for('home'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def show_user_movies(user_id):
    user = User.query.get_or_404(user_id)
    movies = data_manager.get_movies(user_id)
    return render_template('user_movies.html', user=user, movies=movies)



@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_user_movie(user_id):
    movie_title = request.form.get('title')

    movie_data = data_fetch.fetch_data(movie_title) if movie_title else None

    if movie_data:
        movie_obj = {
            'Title': movie_data['title'],
            'Year': movie_data['year'],
            'Director': '',
            'imdbID': '',
            'Poster': movie_data['poster_url']
        }
    else:
        movie_obj = {
            'Title': movie_title,
            'Year': request.form.get('year', ''),
            'Director': request.form.get('director', ''),
            'imdbID': request.form.get('imdb_id', ''),
            'Poster': request.form.get('poster_url', '')
        }

    data_manager.add_movie(user_id, movie_obj)
    return redirect(url_for('show_user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie_title(user_id, movie_id):
    new_title = request.form.get('new_title')
    if new_title and new_title.strip():
        success = data_manager.update_movie(movie_id, new_title.strip())
        if not success:
            flash('Movie not found', 'error')
    return redirect(url_for('show_user_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    success = data_manager.delete_movie(movie_id)
    if not success:
        flash('Movie not found', 'error')
    return redirect(url_for('show_user_movies', user_id=user_id))




if __name__ == '__main__':
  with app.app_context():
    db.create_all()

  app.run()


