
class Movie():

    def __init__(self, title, story, poster, trailer_youtube_url):
        # Sets the movie title, story, image url anad trailer
        self.title = title
        self.story = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_youtube_url

    def __str__(self):
        # Returns the string format of the movie.
        return '[title: {}, story: {}, poster: {}, trailer: {}]'.format(self.title, self.story, self.poster_image_url, self.trailer_youtube_url)
