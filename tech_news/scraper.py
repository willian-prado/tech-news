import requests
import time
from parsel import Selector
# import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news = selector.css("h3.tec--card__title a::attr(href)").getall()
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".tec--btn--primary::attr(href)").get()
    return next_page if (next_page) else None


# def filter_tags(text):
#     return re.sub(r"<[^>]+>", "", text)


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.css("time::attr(datetime)").get()
    writer = selector.css(".z--font-bold *::text").get()
    writer = writer.strip() if (writer) else writer
    shares_count = selector.css("div.tec--toolbar__item::text").re_first(
        r"\d+"
    ) or 0
    comments_count = (
        selector.css("button.tec--btn::attr(data-count)").get()
    )
    summary = "".join(
        selector.css(
            "div.tec--article__body > p:first-child *::text").getall())
    sources = [
        source.strip()
        for source in selector.css("div.z--mb-16 > div > a::text").getall()
    ]
    categories = [
        category.strip()
        for category in selector.css("a.tec--badge--primary::text").getall()
    ]

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "shares_count": int(shares_count) or 0,
        "comments_count": int(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categories,
    }


# Requisito 5
def get_tech_news(amount):
    html_base = fetch('https://www.tecmundo.com.br/novidades')
    news_urls = scrape_novidades(html_base)
    next_page_url = scrape_next_page_link(html_base)
    result = []

    while (len(news_urls) < amount):
        next_page_html = fetch(next_page_url)
        next_page_urls = scrape_novidades(next_page_html)
        news_urls += next_page_urls

    for index in range(0, amount):
        news_html = fetch(news_urls[index])
        dict_news = scrape_noticia(news_html)
        result.append(dict_news)

    create_news(result)
    return result
