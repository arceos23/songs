from flask import Flask, request, Response
from http import HTTPStatus
import constants

def create_app(test_config=None):
    """Return a songs API app."""
    app = Flask(__name__, instance_relative_config=True)

    from . import db


    @app.get(f"{constants.API_VERSION_ONE}/songs")
    def songs():
        """Return a paginated response of songs."""
        title = request.args.get('title', None)
        if title is not None:
            song = db.get_song(title)
            if len(song) == 0:
                return Response(constants.SONG_TITLE_NOT_FOUND_MESSAGE + title, HTTPStatus.NOT_FOUND)
            else:
                return Response(song.to_json(orient='records'), HTTPStatus.OK, mimetype=constants.JSON_MIMETYPE)
        else:
            try:
                start = int(request.args.get('start', constants.PAGINATION_START_DEFAULT))
            except:
                return Response(constants.INVALID_START_DATA_TYPE_MESSAGE, HTTPStatus.BAD_REQUEST)
            try:
                limit = int(request.args.get('limit', constants.PAGINATION_LIMIT_DEFAULT))
            except:
                return Response(constants.INVALID_LIMIT_DATA_TYPE_MESSAGE, HTTPStatus.BAD_REQUEST)

            songs = db.get_songs(start, limit)
            return Response(songs.to_json(orient="records"), HTTPStatus.OK, mimetype=constants.JSON_MIMETYPE)


    @app.patch(f"{constants.API_VERSION_ONE}/songs/<id>")
    def song(id):
        """Update a song's rating and return the updated song."""
        rating = request.form['rating']
        try:
            rating = int(rating)
        except:
            return Response(constants.INVALID_RATING_DATA_TYPE_MESSAGE, HTTPStatus.BAD_REQUEST)

        if not (rating >= constants.RATING_LOWER_BOUND and rating <= constants.RATING_UPPER_BOUND):
            return Response(constants.INVALID_RATING_RANGE_MESSAGE, HTTPStatus.BAD_REQUEST)

        song = db.set_song_rating(id, rating)
        if len(song) == 0:
             return Response(constants.SONG_ID_NOT_FOUND_MESSAGE + id, HTTPStatus.NOT_FOUND)
        else:
            return Response(song.to_json(orient='records'), HTTPStatus.OK, mimetype=constants.JSON_MIMETYPE)

    return app
