import pandas

df = pandas.read_json('data/playlist[76][36][58].json')
df['rating'] = None

def get_songs(start=0, limit=None):
    return df[start:] if limit is None else df[start:start+limit]

def get_song(title):
    return df.loc[df['title'] == title]

def set_song_rating(id, rating):
    df.loc[df['id'] == id, 'rating'] = rating
    return df.loc[df['id'] == id]
