import requests
import tweepy
from bs4 import BeautifulSoup

from config import env

client = tweepy.Client(
    consumer_key=env.API_KEY,
    consumer_secret=env.API_SECRET_KEY,
    access_token=env.ACCESS_TOKEN,
    access_token_secret=env.ACCESS_TOKEN_SECRET,
)


def scrape_todays_top_shayari() -> tuple[str, str]:
    response = requests.get("https://rekhta.org/")
    soup = BeautifulSoup(response.text, "lxml")
    result = soup.find("div", class_="sherLines")
    shayari = result.find("div", class_="c").text
    poet = result.find("span", class_="poetName").text

    return (shayari, poet)


def format_tweet(content: tuple[str, str]) -> str:
    return content[0] + "\n\n" + content[1]


if __name__ == "__main__":
    result = scrape_todays_top_shayari()
    shayari = format_tweet(result)
    client.create_tweet(text=format_tweet(shayari))
