"""Models for Playlist app."""
from app import db
from sqlalchemy.orm import relationship



class Playlist(db.Model):
    """Playlist."""
    id          =   db.Column(db.Integer, primary_key=True)
    name        =   db.Column(db.String())
    description =   db.Column(db.String())

    playlist    =   relationship("PlaylistSong", backref="playlist")

class Song(db.Model):
    """Song."""
    id      =   db.Column(db.Integer, primary_key=True)
    title   =   db.Column(db.String())
    artist  =   db.Column(db.String())

    playlistsongs = relationship("PlaylistSong", backref="song")

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    id          =   db.Column(db.Integer, primary_key=True)
    playlist_id =   db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id     =   db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    # ADD THE NECESSARY CODE HERE



