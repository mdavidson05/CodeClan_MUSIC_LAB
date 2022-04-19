from db.run_sql import run_sql
from models.albums import *
from models.artist import *

def save(artist):
    sql = "INSERT INTO artist(name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql,values)
    id = results[0]['id']
    artist.id = id
    return artist


def select_all():
    artists = []

    sql = "SELECT * FROM artist"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def select(id):
    artist = None

    sql = "SELECT * FROM artist WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)[0]
    if results is not None:
        artist = Artist(results['name'], results['id'])
    return artist

def delete_all():
    sql = "DELETE FROM artist"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM artist WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def update(artist):
    sql = "UPDATE artist SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql,values)
