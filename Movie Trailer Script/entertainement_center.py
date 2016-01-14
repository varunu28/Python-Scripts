import fresh_tomatoes
import media

toystory = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on an alien island","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

social_network = media.Movie("Social Network","How Facebook was built","https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg","https://www.youtube.com/watch?v=lB95KLmpLR4")

godfather = media.Movie("Godfather","A Mario Puzo adaption","https://upload.wikimedia.org/wikipedia/en/b/bd/Mafia!poster.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

karate_kid = media.Movie("Karate Kid","A boy leaning Karatae against all odds","https://upload.wikimedia.org/wikipedia/en/d/d5/Karate_kid_ver2.jpg","https://www.youtube.com/watch?v=2SmmxvHLsKk")

school_of_rock = media.Movie("School of rock","Using music to learn","http://beconfused.s3.amazonaws.com/media/2006/01/School-of-rock-poster.jpg","https://www.youtube.com/watch?v=5afGGGsxvEA")

movies = [toystory ,avatar,social_network ,godfather,karate_kid,school_of_rock]
fresh_tomatoes.open_movies_page(movies)
