DROP TABLE IF EXISTS song;

CREATE TABLE song (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  external_id TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  danceability REAL,
  energy REAL,
  key INTEGER,
  loudness REAL,
  mode INTEGER,
  acousticness REAL,
  instrumentalness REAL,
  liveness REAL,
  valence REAL,
  tempo REAL,
  duration_ms INTEGER,
  time_signature INTEGER,
  num_bars INTEGER,
  num_sections INTEGER,
  num_segments INTEGER,
  class INTEGER,
  rating INTEGER CHECK (rating >= 0 AND rating <= 5)
);
