from app import app, db
from app.models import Playlist, Song, PlaylistSong


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Playlist': Playlist,"Song":Song,"PlaylistSong":PlaylistSong}