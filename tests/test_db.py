import app.db as db
import constants


def test_ingestion():
    assert len(db.df) == constants.NUMBER_OF_SONGS
    assert len(db.df.columns) == constants.NUMBER_OF_ATTRIBUTES


def test_get_songs():
    songs = db.get_songs()
    assert len(songs) == constants.NUMBER_OF_SONGS

    songs = db.get_songs(1, 3)
    assert len(songs) == 3


def test_get_song():
    song = db.get_song("4 Walls")
    assert len(song) == 1
    assert len(song.columns) == constants.NUMBER_OF_ATTRIBUTES
    assert song.loc[1, "id"] == "2klCjJcucgGQysgH170npL"
    assert song.loc[1, "title"] == "4 Walls"
    assert song.loc[1, "danceability"] == 0.735
    assert song.loc[1, "energy"] == 0.849
    assert song.loc[1, "key"] == 4
    assert song.loc[1, "loudness"] == -4.308
    assert song.loc[1, "mode"] == 0
    assert song.loc[1, "acousticness"] == 0.212
    assert song.loc[1, "instrumentalness"] == 0.0000294
    assert song.loc[1, "liveness"] == 0.0608
    assert song.loc[1, "valence"] == 0.223
    assert song.loc[1, "tempo"] == 125.972
    assert song.loc[1, "duration_ms"] == 207477
    assert song.loc[1, "time_signature"] == 4
    assert song.loc[1, "num_bars"] == 107
    assert song.loc[1, "num_sections"] == 7
    assert song.loc[1, "num_segments"] == 999
    assert song.loc[1, "class"] == 1
    assert song.loc[1, "rating"] == None


def test_set_song_rating():
    song = db.set_song_rating("2klCjJcucgGQysgH170npL", 2)
    assert len(song) == 1
    assert len(song.columns) == constants.NUMBER_OF_ATTRIBUTES
    assert song.loc[1, "id"] == "2klCjJcucgGQysgH170npL"
    assert song.loc[1, "title"] == "4 Walls"
    assert song.loc[1, "danceability"] == 0.735
    assert song.loc[1, "energy"] == 0.849
    assert song.loc[1, "key"] == 4
    assert song.loc[1, "loudness"] == -4.308
    assert song.loc[1, "mode"] == 0
    assert song.loc[1, "acousticness"] == 0.212
    assert song.loc[1, "instrumentalness"] == 0.0000294
    assert song.loc[1, "liveness"] == 0.0608
    assert song.loc[1, "valence"] == 0.223
    assert song.loc[1, "tempo"] == 125.972
    assert song.loc[1, "duration_ms"] == 207477
    assert song.loc[1, "time_signature"] == 4
    assert song.loc[1, "num_bars"] == 107
    assert song.loc[1, "num_sections"] == 7
    assert song.loc[1, "num_segments"] == 999
    assert song.loc[1, "class"] == 1
    assert song.loc[1, "rating"] == 2
