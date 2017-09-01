class Movie(object):
	"""Stores the movie data.

    Attributes:
        title: String of movie title.
        poster_image_url: String of poster url image.
        trailer_youtube_url: String of youtube trailer
        url.
    """

    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
