import urllib.request,json
from app.models import Articles,Source


# Getting api key
apiKey = None
base_url = None
article_url = None

def configure_request(app):
    global apiKey,base_url,article_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']
