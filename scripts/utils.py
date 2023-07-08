""" This file contains utility functions for the project """

from bs4 import BeautifulSoup
import requests
import re

def get_soup(url):
    """ Returns a BeautifulSoup object for the given url """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    return soup

def get_title_and_year_from_h1(h1_text):
    """ Returns the title and year from the given h1 tag """
    h1_regex = '^(.*) \(([0-9]{4})\) - full transcript$'
    title = re.search(h1_regex, h1_text).group(1)
    year = re.search(h1_regex, h1_text).group(2)
    return title, int(year)

def clean_title(title):
    """ Returns a title cleaned from characters that cannot be used in a file name"""
    regex = '[/\\|<>*.:?"]'
    return re.sub(regex, '', title)

# test functions
# print(get_title_and_year_from_h1('99 (2009) - full transcript'))