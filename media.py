import webbrowser

class Movie():
    # The constructor for the movie object, takes in essential information for the movie
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    # Opens a web-browser to the trailer URL in order to display the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
