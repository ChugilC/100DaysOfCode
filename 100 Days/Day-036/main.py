import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "YOUR_KEY_HERE"
NEWS_API_KEY = "TOUR_KEY_HERE"

STOCK_PARAMETERS = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

NEWS_PARAMETERS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
data = response.json()["Time Series (Daily)"]


data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))

diff_percentage = (difference / float(yesterday_closing_price)) * 100

if diff_percentage > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    
    formatted_articles = [f"Headline: {article['title']}, \nBrief: {article['description']}" for article in three_articles]