# Scraping Movies Transcripts with BeautifulSoup

## Description

In this project, we are going to look at the [sublikescript](https://subslikescript.com/) website about movies, and then use Python and the beautifulsoup library in order to get a list of movies titles, dates and descriptions. The output datasets could be used for machine learning and analysis tasks.

## Output Datasets

In the data folder:

- `movies_data`: folder where I put the datasets about movies titles, dates and descriptions.
- `movies_transcript`: folder where I put transcriptions files for each movie in the movies_data datasets. We'll have a sub folder for each first letter in the title.

Note that we are not going to get all the movies in the website, but for each letter that the movie's title might start with, we'll get the first 2 pages of content.

## How to use

You can either download the datasets for applying machine learning or NLP tasks, or play with the scripts in order to do the same task for TV shows instead of movies.

## Setup

Run the following command for installing the required dependencies:

`pip install -r requirements.txt`

## Tools & Libraries

- Python 3.10
- pandas (data manipulation library)
- beautifulsoup (scraping library)

## Aknowledgements

Thanks to [Frank Andrade](https://www.udemy.com/user/frank-andrade-13/) aka The Pycoach for his great course on web scraping.
