from app import app, db,Config

from flask import  flash, redirect, render_template, request, session, abort,url_for

from app.models import Playlist, Song, PlaylistSong
from app.forms import NewSongForPlaylistForm, SongForm, PlaylistForm

import os



@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.filter_by(id=playlist_id).first()
    playlistsong = PlaylistSong.query.filter_by(playlist_id=playlist_id).all()
  
    return render_template('playlist.html',playlist=playlist,playlistsong=playlistsong)

@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:
    
    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    if form.validate_on_submit():
        playlist = Playlist(name = form.name.data,description=form.description.data)
        db.session.add(playlist)
        db.session.commit()
        return redirect(url_for('show_all_playlists'))
    return render_template('new_playlist.html', form=form)
    


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""
    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song = Song.query.filter_by(id=song_id).first()
    playlistsongin = PlaylistSong.query.filter_by(song_id=song_id).all()

    return render_template('song.html',song=song,playlistsongin=playlistsongin)
   

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    if form.validate_on_submit():
        song = Song(title=form.title.data,artist=form.artist.data)
        db.session.add(song)
        db.session.commit()
        return redirect(url_for('show_all_songs'))
    return render_template('new_song.html',form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist
    raw_sql = """SELECT 
                    id
                FROM 
                    song
                WHERE
	                song.id NOT IN (SELECT 
                                        song_id 
                                    FROM 
                                        playlist_song
                                    WHERE playlist_id=%s)"""
    query_result = db.engine.execute(raw_sql,(playlist_id,))
    x =  [dict(row) for row in query_result]
    y = []
    for item in x:
        y.append(item["id"])
    form.song.choices = y

    if form.validate_on_submit():
        playlistsong = PlaylistSong(playlist_id=playlist_id,song_id=form.song.data)
        db.session.add(playlistsong)
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
