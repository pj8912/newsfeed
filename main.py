from flask import Flask, render_template, request
from feed import *


app = Flask(__name__)

@app.route('/')
@app.route("/news/feed/1")
def home():
    news_list = [
        "https://www.news18.com/rss/india.xml",
        "https://www.news18.com/rss/world.xml",
        "https://www.timesofisrael.com/feed/",
        "https://www.news18.com/commonfeeds/v1/eng/rss/viral.xml"
    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 1")




@app.route("/news/feed/2")
def feed_2():
    news_list =   [
        "https://www.indiatoday.in/rss/1206577",
        "https://aninews.in/rss/feed/category/national/politics.xml",
        "https://www.thehindu.com/sci-tech/science/feeder/default.rss",
        "http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 2")


@app.route("/news/feed/3")
def feed_3():
    news_list = [
    "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
    "https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms",
    "https://www.news18.com/commonfeeds/v1/eng/rss/politics.xml",
    "https://www.news18.com/commonfeeds/v1/eng/rss/sports.xml"
    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 3")


@app.route("/news/feed/4")
def feed_4():
    news_list = [
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/US.xml",
        "https://tamil.asianetnews.com/rss",
        "https://www.thehindu.com/news/international/feeder/default.rss"

    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 4")


@app.route("/news/feed/5")
def feed_5():
    news_list = [
        "https://www.news18.com/commonfeeds/v1/eng/rss/india.xml",
    "https://tamil.goodreturns.in/rss/tamil-money-news-fb.xml",
    "https://tamil.gizbot.com/rss/gizbot-tamil-fb.xml",
    "https://tamil.oneindia.com/rss/feeds/oneindia-tamil-fb.xml"
]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 5")


@app.route("/news/feed/6")
def feed_6():
    news_list = [
    "https://www.vikatan.com/stories.rss",
    "https://rss.dinamalar.com/?cat=ara1",
    "https://tamil.filmibeat.com/rss/feeds/filmibeat-tamil-fb.xml",
    "https://tamil.mykhel.com/rss/feeds/mykhel-tamil-fb.xml"
    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 6")

@app.route("/news/feed/7")
def feed_7():
    news_list = [
    "https://tamil.oneindia.com/rss/feeds/oneindia-tamil-fb.xml",
    "https://feeds.feedburner.com/Hindu_Tamil_world",
    "https://lemmy.world/feeds/c/technology.xml?sort=Active",
    "https://feeds.feedburner.com/Hindu_Tamil_india"
    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 7")

@app.route("/news/feed/8")
def feed_8():
    news_list = [
    "https://tamil.news18.com/commonfeeds/v1/tam/rss/national.xml",
    "https://feeds.feedburner.com/ndtvnews-top-stories",
    "https://feeds.feedburner.com/ndtvnews-india-news",
    "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN"
    ]

    result = combined_feeds(news_list)
    return render_template('base.html', data=result, title="feed 8")


if __name__ == '__main__':
    app.run(debug=True)