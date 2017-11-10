import webbrowser

class Movie():
    """ This class provides a way to store movie related information

    Args:
        movie_title (str): Title of movie
        movie_storyline (str): Brief description of the story line of the movie
        poster_image (str): URL of an image to be used for the movie ie poster
        trailer_youtube (str): URL of a trailer video for the movie

    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
