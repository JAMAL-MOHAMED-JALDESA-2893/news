import urllib.request
import json
from .models import Sources, Articles


# Getting api key
api_key = None

# Getting the news base url
base_url =None

# Getting the news articles base url
articles_base_url = None


def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_base_url = app.config['ARTICLES_BASE_URL']