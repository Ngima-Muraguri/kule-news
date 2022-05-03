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


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,apiKey)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = None
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
    return source_results

def process_results(source_list):
    
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
   
        source_object = Source(id,name,description,url,category)
        source_results.append(source_object)

    return source_results

def get_source(id):
    get_source_details_url = base_url.format(id,apiKey)
    with urllib.request.urlopen(get_source_details_url) as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)
        source_object = None
        if source_details_response:
            id = source_details_response.get('id')
            name = source_details_response.get('name')
            description = source_details_response.get('description')
            url= source_details_response.get('url')
            category = source_details_response.get('category')
            source_object = Source(id,name,description,url,category)

    return source_object

def get_article(id):
    '''
    A function that returns a list of articles
    '''
    get_articles_details_url = article_url.format(id,apiKey)
    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)
        articles_object = None
        if articles_details_response:
            author = articles_details_response('author')
            title = articles_details_response('title')
            description = articles_details_response.get('description')
            url= articles_details_response.get('url')
            urlToImage = articles_details_response.get('urlToImage')
            publishedAt = articles_details_response.get('publishedAt')
            content = articles_details_response.get('content')
        
            articles_object = Articles(title,author,description,url,urlToImage,publishedAt,content)

    return articles_object

def get_articles(source):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(source,apiKey)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        articles_results = []
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)
    return articles_results

def process_articles_results(articles_list):
    
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url= articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')
        
   
        articles_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(articles_object)

    return articles_results
