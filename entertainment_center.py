import media
import fresh_tomatoes

# Initialize all movies to be displayed on the website
october_sky = media.Movie("October Sky",
                        "A story of a boy who builds rockets",
                        "http://static.rogerebert.com/uploads/movie/movie_poster/october-sky-1999/large_hEHrAkdyCVGpIIxioLP7rB1zKUf.jpg",# NOQA
                        "https://www.youtube.com/watch?v=zxJQgYPXjN4")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://static.rogerebert.com/uploads/movie/movie_poster/avatar-2009/large_8Ic8rRVoVrDJJlXzVzGxAesufUV.jpg", # NOQA
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

star_wars = media.Movie("Star Wars",
                        "A lot of needless violence in space",
                        "http://cdn.shopify.com/s/files/1/1083/5290/products/Swtfa_-_One_Sheet_Movie_Poster_RP14353_UPC882663043538_Star_Wars_The_Force_Awakens_grande.jpg", # NOQA
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

elf = media.Movie("Elf",
                  "A boy gets kidnapped and raised by Santa",
                  "http://www.scholastic.com/100movies/assets/53_elf_00.jpg", # NOQA
                  "https://www.youtube.com/watch?v=gW9wRNqQ_P8")

guardians = media.Movie("Guardians of the Galaxy",
                        "A group of outcasts and a talking racoon play tag across the galaxy",
                        "http://www.vintagestock.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/6/160138.jpg", # NOQA
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")

iron_man = media.Movie("Iron Man 3",
                        "A guy with a cool suit blows stuff up",
                        "http://static.rogerebert.com/uploads/movie/movie_poster/iron-man-3-2013/large_kC4NM99bJ5Xq03O6XQ6602GKRsi.jpg", # NOQA
                        "https://www.youtube.com/watch?v=oYSD2VQagc4")

# Put movies into an array to get passed into the website
movies = [october_sky, avatar, star_wars, elf, guardians, iron_man]

# Generate the webpage using the array of movies, and display the page
fresh_tomatoes.open_movies_page(movies)
