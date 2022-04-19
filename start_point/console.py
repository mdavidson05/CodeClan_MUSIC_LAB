import pdb
from models.albums import *
from models.artist import *
import repositories.albums_repository as album_repository
import repositories.artist_repository as artist_repository

########## this is not always required - to reset databse

album_repository.delete_all()
artist_repository.delete_all()

artist = Artist('Prince')
artist_repository.save(artist)

artist2 = Artist('Foo Fighters')
artist_repository.save(artist2)

# user_repository.select_all()

album = Albums('Kiss', 'Rock', artist)
album_repository.save(album)


#pdb.set_trace()
