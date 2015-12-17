import webbrowser

class Movie():
    #RATING={'G':'G','PG':'PG','R': 'R'}  In this example how could one call this in the entertainment_center.py file??
    #I know that this is supposed to be a best practice but the material did not cover how this could be called
    #in from other files.


    def __init__(self, movie_title, movie_storyline, genre, duration, cast,
    poster_image, trailer_youtube_url, year_release,rating,star_review):
        self.title=movie_title
        self.movie_storyline=movie_storyline
        self.genre=genre
        self.duration=duration
        self.cast=cast
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube_url
        self.year_release=year_release
        self.rating=rating
        self.star_review=star_review


    def start_movie(self):
        webbrowser.open(self.trailer_youtube)
