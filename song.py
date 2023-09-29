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


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__== '__main__':
    load_data()
























