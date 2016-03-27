import unittest

from src.movie import Movie;

class MovieTest(unittest.TestCase):

    def test_movie_init(self):
        movie = Movie("Some title", "Some story", "Some poster", "Some trailer")
        self.assertEqual(movie.title, "Some title")
        self.assertEqual(movie.story, "Some story")
        self.assertEqual(movie.poster_image_url, "Some poster")
        self.assertEqual(movie.trailer_youtube_url, "Some trailer")

    def test_movie_str(self):
        movie = Movie("Some title", "Some story", "Some poster", "Some trailer")
        self.assertEqual(movie.__str__(),
                         '[title: {}, story: {}, poster: {}, trailer: {}]'.format(
                             movie.title,
                             movie.story,
                             movie.poster_image_url,
                             movie.trailer_youtube_url))