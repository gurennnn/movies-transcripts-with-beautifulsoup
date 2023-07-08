""" Main script for scraping the movies transcripts and info from subslikescript.com """

# import the necessary libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
from utils import *
import re
import os

print('Starting scraping...')

# base url
root_url = 'https://subslikescript.com'

# create a BeautifulSoup object
movies_soup = get_soup(f'{root_url}/movies')

"""
We are going to scrape the movies for each letter of the alphabet.
"""

# get the links for each letter
letters_links = [link.get('href') for link in movies_soup.find_all('a', {'href': re.compile('/movies_letter-([A-Z]|sign)')})]

# loop through each letter link
for letter_link in letters_links[1:4]:

    # create a directory for the current letter if it doesn't exist
    letter = letter_link.split('-')[-1]
    if os.path.exists(f'../data/movies_transcripts/{letter}') == False:
        os.mkdir(f'../data/movies_transcripts/{letter}')

    # initialize empty lists for storing movie info
    titles = []
    years = []
    plots = []

    link = f'{root_url}{letter_link}'
    letter_movies_soup = get_soup(link)
    
    # get number of pages
    nav = letter_movies_soup.find('nav', class_='pagination_pages')
    n_pages = int(nav.find_all('a')[-2].text)
    n_pages_to_scrape = 1
    
    print(f'\n########## Scraping movies for letter {letter}... ##########')

    # scrape the first 2 pages of each letter
    for n_page in range(1, n_pages + 1)[:n_pages_to_scrape]:

        print(f'\nScraping page {n_page}...')

        soup = get_soup(f'{link}?page={n_page}')
        movies_article = soup.find('article', class_='main-article')
        movies_links = [link.get('href') for link in movies_article.find_all('a')]

        for movie_link in movies_links:

            movie_soup = get_soup(f'{root_url}/{movie_link}')
            movie_article = movie_soup.find('article', class_='main-article')
            
            movie_title, movie_year = get_title_and_year_from_h1(movie_article.find('h1').text)

            print(f'Scraping movie {movie_title}...')

            # sometimes the plot is not available
            try:
                movie_plot = movie_article.find('p', class_='plot').text
            except:
                movie_plot = 'Not available'
            # save movie info
            titles.append(movie_title)
            years.append(movie_year)
            plots.append(movie_plot)
            
            # save movie transcript
            movie_transcript = movie_article.find('div', class_='full-script').get_text(strip=True, separator='\n')
            movie_title = clean_title(movie_title)
            with open(f'../data/movies_transcripts/{letter}/{movie_title}.txt', 'w') as f:
                f.write(movie_transcript)

        print(f'Done scraping page {n_page}.')

    # save movie info to csv
    df = pd.DataFrame({'title': titles, 'year': years, 'plot': plots})
    df.to_csv(f'../data/movies_info/{letter}.csv', index=False)

    print(f'Done scraping movies for letter {letter}.')

print('Done scraping movies.')
