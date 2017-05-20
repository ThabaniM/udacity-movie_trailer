#some code borrowed from class examlple in udacity lectures

import webbrowser

# this is how a class is defined in this case it's called Movie
class Movie():
   
     # when an instance is created this the function/method called
     def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

         self.title = movie_title
         self.storyline = movie_storyline
         self.poster_image_url = poster_image
         self.trailer_youtube_url = trailer_youtube


     def show_trailer(self): 
         webbrowser.open(self.trailer_youtube_url)
         
      





         
