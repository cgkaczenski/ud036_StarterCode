import fresh_tomatoes as ft
import media

mulholland = media.Movie(
    "Mulholland Drive",
    "https://upload.wikimedia.org/wikipedia/en/0/0f/Mulholland.png",
    "https://www.youtube.com/watch?v=jbZJ487oJlY")

eyes = media.Movie(
    "Eyes Wide Shut",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Eyes_Wide_Shut_poster.jpg",
    "https://www.youtube.com/watch?v=_0sJwdgB2Q8")

vertigo = media.Movie(
    "Vertigo",
    "https://upload.wikimedia.org/wikipedia/commons/7/75/Vertigomovie_restoration.jpg",
    "https://www.youtube.com/watch?v=trDqSL_RAsY")

prestige = media.Movie(
    "The Prestige",
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
    "https://www.youtube.com/watch?v=o4gHCmTQDVI")

day = media.Movie(
    "Day for Night",
    "https://upload.wikimedia.org/wikipedia/en/2/20/La_Nuit_oscar.jpg",
    "https://www.youtube.com/watch?v=DKoEVBHMp3s")

movies = [mulholland, eyes, vertigo, prestige, day]

ft.open_movies_page(movies)
