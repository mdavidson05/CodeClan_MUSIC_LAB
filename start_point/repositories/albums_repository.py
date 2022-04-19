from db.run_sql import run_sql
from models.albums import *
from models.artist import *
import repositories.artist_repository as art_repo

def save(album):
    sql = "INSERT INTO albums(title, genre, artist_id) VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = art_repo.select[row('artist_id')]
        album = Albums(row['title'], row['genre'], artist)
        albums.append(album)
    return albums

def select(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)[0]
    if results is not None:
        artist = art_repo.select[('artist_id')]
        album = Albums(['title'], ['genre'], artist)
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(albums):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s) WHERE id = %s"
    values = [albums.title, albums.genre, albums.artist.id]
    run_sql(sql,values)



