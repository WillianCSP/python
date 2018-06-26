import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A historia de um menino",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)
avatar = media.Movie("Avatar","Azuis",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
