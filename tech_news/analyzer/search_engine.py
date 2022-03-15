from tech_news.database import search_news
from datetime import datetime, timedelta


# Requisito 6
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    title_tuple = [(report["title"], report["url"]) for report in news]
    return title_tuple


# Requisito 7
def search_by_date(date):
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    news = search_news({
        "timestamp": {
            "$lt": datetime.isoformat(format_date + timedelta(days=1)),
            "$gte": datetime.isoformat(format_date)
        }
    })

    title_tuple = [(report["title"], report["url"]) for report in news]
    return title_tuple


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": {"$regex": source, "$options": "i"}})
    title_tuple = [(report["title"], report["url"]) for report in news]
    return title_tuple


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
