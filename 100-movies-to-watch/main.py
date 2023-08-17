import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
# response.text is all the HTML from the website attached to the URL.
website_html = response.text
# BeautifulSoup parses the content (website_html) without a specific parser for the file (html.parser).
soup = BeautifulSoup(website_html, "html.parser")
# Finds all the <h3> tags with a class of title.
all_movies = soup.find_all(name="h3", class_="title")
# Creates a dictionary of all the text from the tags.
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
