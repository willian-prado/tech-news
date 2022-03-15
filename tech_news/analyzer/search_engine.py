from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {'$regex': title, '$options': 'i'}})
    title_tuple = [(report['title'], report['url']) for report in news]
    return title_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
