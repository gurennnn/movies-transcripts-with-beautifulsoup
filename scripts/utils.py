""" This file contains utility functions for the project """

from bs4 import BeautifulSoup
import requests

def get_soup(url):
    """ Returns a BeautifulSoup object for the given url """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    return soup

