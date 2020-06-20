from flask import render_template, url_for, redirect, request
from application import app, db, bcrypt
from application.models import Playlists, Users, Songs
from application.forms import  RegistrationForm, LoginForm, UpdateAccountForm, UpdatePlaylistForm, SongsForm, PlaylistForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/home')
@app.route('/')
def home():
    all_playlists = Playlists.query.all()
    return render_template('home.html', title='Home', playlists=all_playlists)


@app.route('/about')
def about():
    return render_template('about.html', title='About', info='this is the about page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)


@app.route('/account/delete', methods=['GET', 'POST'])
@login_required
def account_delete():
    user = current_user.id
    playlists = Playlists.query.filter_by(user_id=user)
    for playlist in playlists:
        db.session.delete(playlist)
    account = Users.query.filter_by(id=user).first()
    logout_user()
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('register'))

@app.route('/playlist', methods=['GET', 'POST'])
@login_required
def playlist():
    form = PlaylistForm()
    if form.validate_on_submit():
        new_playlist = Playlists(
            title=form.title.data,
            songs_id=form.content1.data,
            songs_id2=form.content2.data,
            songs_id3=form.content3.data,
            author=current_user
        )
        db.session.add(new_playlist)
        db.session.commit()
        return redirect(url_for('home'))
    all_songs = Songs.query.all()
    song_choices = []
    for song in all_songs:
        song_choices.append((song.id, song.title))
    form.content1.choices=song_choices
    form.content2.choices=song_choices
    form.content3.choices=song_choices
    return render_template('playlist.html', title='Playlist', form=form)

@app.route('/playlist/delete/<int:playlists_id>', methods=['GET', 'POST'])
@login_required
def playlist_delete(playlists_id):
    playlist = Playlists.query.filter_by(id=playlists_id).first()
    db.session.delete(playlist)
    db.session.commit()
    return redirect(url_for('home'))  

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                password=hash_pw
                )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('add_songs'))
    return render_template('register.html', title='Register', form=form )

@app.route('/songs', methods=['GET', 'POST'])
@login_required
def add_songs():
    form = SongsForm()
    if form.validate_on_submit():
        new_song = Songs(
                title=form.song_name.data,
                artist=form.song_artist.data,
        )

        db.session.add(new_song)        
        db.session.commit()
        return redirect(url_for('add_songs'))
    all_songs = Songs.query.all()
    return render_template('songs.html', title='Songs', form=form, songs=all_songs)

@app.route('/song/delete/<int:song_id>', methods=['GET', 'POST'])
@login_required
def song_delete(song_id):
    song = Songs.query.filter_by(id=song_id).first()
    db.session.delete(song)
    db.session.commit()
    return redirect(url_for('add_songs'))

@app.route('/update/playlist/<int:playlist_id>', methods=['GET', 'POST'])
@login_required
def playlist_update(playlist_id):
    form = UpdatePlaylistForm()
    playlist = Playlists.query.filter_by(id=playlist_id).first()
    all_songs = Songs.query.all()
    song_choices = []
    for song in all_songs:
        song_choices.append((song.id, song.title))
    form.content1.choices=song_choices
    form.content2.choices=song_choices
    form.content3.choices=song_choices
    if form.validate_on_submit():
        playlist.songs_id=form.content1.data
        playlist.songs_id2=form.content2.data
        playlist.songs_id3=form.content3.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update.html', title='Update', form=form, playlist_id=playlist_id)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
