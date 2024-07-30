from flask import Flask, request
from db import get_songs, get_song, set_song_rating

VERSION_PRFEFIX = "/api/v1"

app = Flask(__name__)

@app.get(f"{VERSION_PRFEFIX}/songs")
def songs():
    title = request.args.get('title', None)
    if title is not None:
        song = get_song(title)
        return song.to_json(orient='records'), 200
    else:
        start = int(request.args.get('start', 0))
        limit = int(request.args.get('limit', 5))
        songs = get_songs(start, limit)
        return songs.to_json(orient="records"), 200

@app.post(f"{VERSION_PRFEFIX}/songs/<id>")
def song(id):
    rating = request.form['rating']
    try:
        rating = int(rating)
    except:
        return "Rating must be an integer between 0 and 5.", 400

    if not (rating >= 0 and rating <= 5):
        return "Rating must be between 0 and 5.", 400

    song = set_song_rating(id, rating)
    return song.to_json(orient='records'), 200
