import fresh_tomatoes as ft
import media

mulholland = media.Movie("Mulholland Drive", "https://upload.wikimedia.org/wikipedia/en/0/0f/Mulholland.png", "https://www.youtube.com/watch?v=jbZJ487oJlY")
eyes = media.Movie("Eyes Wide Shut", "https://upload.wikimedia.org/wikipedia/en/8/87/Eyes_Wide_Shut_poster.jpg", "https://www.youtube.com/watch?v=_0sJwdgB2Q8")

movies = [mulholland, eyes]

ft.open_movies_page(movies)