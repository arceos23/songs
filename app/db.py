import sqlite3
import click
import app.ingest
from flask import current_app, g
import constants


def get_db():
    current_app.config['DATABASE'] = 'app.sqlite'
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    app.ingest.ingest('app.sqlite', './app/data/playlist[76][36][58].json')


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def get_songs(start, limit=constants.PAGINATION_LIMIT_DEFAULT):
    db = get_db()
    songs = db.execute(
        """ SELECT *
            FROM song
            LIMIT ?
            OFFSET ?
        """,
        (limit, start)
    ).fetchall()
    return songs


def get_song(title):
    db = get_db()
    song = db.execute(
        """ SELECT *
            FROM song
            WHERE title = ?
        """,
        (title,)
    ).fetchall()
    return song


def set_song_rating(id, rating):
    db = get_db()
    song = db.execute(
        """ UPDATE song
            SET rating = ?
            WHERE id = ?
            RETURNING *
        """,
        (rating, id)
    ).fetchall()
    db.commit()
    return song
