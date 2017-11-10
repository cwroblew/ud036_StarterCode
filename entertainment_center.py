import fresh_tomatoes
import media


def create_movie_list():
    movies = {}
    movies["toy_story"] = media.Movie(
        "Toy Story",
        "A story of a boy and his toys that come to life",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "https://www.youtube.com/watch?v=vwyZH85NQC4"
    )

    movies["star_wars"] = media.Movie(
        "Star Wars",
        "The Imperial Forces -- under orders from cruel Darth Vader -- hold Princess "
        "Leia hostage, in their efforts to quell the rebellion against the Galactic "
        "Empire. Luke Skywalker and Han Solo captain of the Millennium Falcon, work " 
        "together with the companionable droid duo R2-D2 and C-3PO to rescue the " 
        "beautiful princess, help the Rebel Alliance, and restore freedom and justice to " 
        "the Galaxy.",
        "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
        "https://www.youtube.com/watch?v=1g3_CFmnU7k"
    )

    movies["wizard_of_oz"] = media.Movie(
        "Wizard of Oz",
        "Dorothy and her dog, Toto, are flown away in their house by a tornado to the " 
        "magical land of Oz. They follow the Yellow Brick Road to get to Emerald City " 
        "to talk to the Wizard. In their travels meet a Scarecrow that needs a brain, " 
        "a Tin Man missing a heart, and a Cowardly Lion who wants courage. The wizard " 
        "tells them that they must bring him the broom of the Wicked Witch of the " 
        "West to get help.",
        "https://upload.wikimedia.org/wikipedia/commons/c/ca/WIZARD_OF_OZ_ORIGINAL_POSTER_1939.jpg",  # NOQA
          "https://www.youtube.com/watch?v=VNugTWHnSfw"
    )
    return movies

movies = create_movie_list()

fresh_tomatoes.open_movies_page(movies)

