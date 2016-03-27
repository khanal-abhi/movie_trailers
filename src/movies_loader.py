from movie import Movie
import fresh_tomatoes

def loadMovies(movies):
    # Open up the movies and show them in the browser.
    fresh_tomatoes.open_movies_page(movies)


if __name__ == "__main__":
    # This method is called if this file (movies_loader.py) is the primary file been run.

    # Declare an empty list to hold the movies
    movies = []

    # Create new movies and append to the newly created list.
    movies.append(Movie(
        "The Shawshank Redemption",
        "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
        "https://www.youtube.com/watch?v=6hB3S9bIaco"
    ))
    movies.append(Movie(
        "The Godfather",
        "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
        "https://www.youtube.com/watch?v=w0VGcWHkNeA"
    ))
    movies.append(Movie(
        "The Dark Knight",
        "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
        "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
        "https://www.youtube.com/watch?v=_PZpmTj1Q8Q"
    ))

    # Call the loadMoviews method to load the newly set up movies list.
    loadMovies(movies)