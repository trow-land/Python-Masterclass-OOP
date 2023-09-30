# Docstrings (below is slightly too verbose) (PEP257)
class Song:
    """
    Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds - may be zero
    """
    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): An Artist object representing the song's creator
            duration (Optional[int]: Initial value for the 'duration'
                Will default to zero if not specified
        """

        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song.__init__)  # Shows the docstring
# print(Song.__doc__)  # Shows class doc string
# print(Song.__init__.__doc__)  # Shows init docstring

class Album:
    """ Class to represent an Album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist: (Artist): The artist responsible for the album.
            If not specified the artist will default to an artist
            with the name "Various Artists"
        tracks (list[song]): A list of the songs on the album

        Methods:
            add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """adds a song to the tracklist

        Args:
            song (Song): A song to add
            position (Optional [int]): if specified the song will be added to that position in
            the tracklist - inserting between other songs if necessary. Otherwise the song will
            appear at the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """ Class to represent the music creator details

    Attributes:
        name (str): Name of the artist
        albums (list[Album]): A list of the albums by this artist
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artists published albums


    Methods:
        add_album: use to add a new album to the artists albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ Add a new album to the list

        Args:
            album (Album): Album object to add to the list
                If the album is already present, it will not be added again (NOT IMPLEMENTED YET)
        """

        self.albums.append(album)

# Garbage collection -> how objects that are no longer used are delt with.

def find_object(field, object_list):
    """ check object_list to see if an object with a name equal to attribute equal to 'field' exists, return it if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, ":", album_field, ":", year_field, ":", song_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # retrieve the artist object if it exists, otherwise we create one and add to artist list
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # retrieve the album object if there is one, else we create it and add to artist's collection
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current albums collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    """ create a check file from the object data for comparison with the original file"""

    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)



if __name__ == '__main__':
    artists = load_data()

print("There are {} artists".format(len(artists)))

create_checkfile(artists)






















