import pandas

df = pandas.read_json('./app/data/playlist[76][36][58].json')
df['rating'] = None

def get_songs(start=0, limit=None):
    """Return the songs based on the start and limit parameters."""
    return df[start:] if limit is None else df[start:start+limit]


def get_song(title):
    """Return the song based on the title parameter."""
    return df.loc[df['title'] == title]


def set_song_rating(id, rating):
    """ Update the rating of the song based on the id and rating parameters and
    return the song. 
    """
    df.loc[df['id'] == id, 'rating'] = rating
    return df.loc[df['id'] == id]
