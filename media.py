    """  Like a database table this class is set up to capture data elements pertinent to
    various films to be listed in the entertainment_center.py file.
    """

    #This is a class variable to be used for data integrity purposes. This variable will be tested and
    # assigned as an instance variable called 'rating'
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

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

        # Check rating input is valid in VALID_RATINGS list
        if rating in self.VALID_RATINGS:
            # Assigns a rating property to rating input if it is  valid
            self.rating=rating
        else:
            # Assigns an invalid string if rating is not valid
            self.rating="INVALID_ENTRY"

    # this function opens the video trailer once selected.
    def start_movie(self):
        webbrowser.open(self.trailer_youtube)
