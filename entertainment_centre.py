#some code borrowed from class examlple in udacity lectures
import media                  
import fresh_tomatoes

# I create 6 instance of class Movie below with four instance variables defined in the class

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that came to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sr/archive/b/b0/20091214155149!Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_lego_movie = media.Movie("The Lego Movie",
                             "An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant",
                             "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSCjPc6MD7zkEdDO3WoFzsRFM_M54KGsVTsxPDC_TjtcAIr5L_p",
                             "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

the_dictator = media.Movie("The Dictator",
                           "The heroic story of a dictator who risked his life to ensure that democracy would never come to the country he so lovingly oppressed",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/The_Dictator_Poster.jpg",
                           "https://www.youtube.com/watch?v=cYplvwBvGA4")
    
#creating an array to be used by the freshtomatoes method open_movies_page(array)

movies = [toy_story,avatar,edge_of_tomorrow,the_matrix, the_lego_movie,the_dictator]
fresh_tomatoes.open_movies_page(movies)


