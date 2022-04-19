DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS albums;

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100),
  genre VARCHAR(100),
  artist_id INT REFERENCES artist(id)
);



