
class Movie():

    def __init__(self, title, story, poster, trailer_youtube_id):
        self.title = title
        self.story = story
        self.poster = poster
        self.trailer_youtube_id = trailer_youtube_id

    def __str__(self):
        return '[title: {}, story: {}, poster: {}, trailer: {}]'.format(self.title, self.story, self.poster, self.trailer_youtube_id)
