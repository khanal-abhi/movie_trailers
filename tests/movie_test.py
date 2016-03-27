import unittest

from src.movie import Movie;


class MovieTest(unittest.TestCase):

    def test_movie_init(self):
        movie = Movie("Some title", "Some story", "Some poster", "Some trailer")
        self.assertEqual(movie.title, "Some title")
        self.assertEqual(movie.story, "Some story")
        self.assertEqual(movie.poster, "Some poster")
        self.assertEqual(movie.trailer_youtube_id, "Some trailer")