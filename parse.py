import datetime
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def main():
    """парсинг событий с python.org"""
    res = requests.get('https://python.org')
    soup = BeautifulSoup(res.text, "lxml")

    # текущий и следующий месяц для проверки
    month_current = datetime.datetime.today().month
    month_next = (datetime.datetime.today() + datetime.timedelta(weeks=4)).month
    event = []

    # вытаскиваем события
    for tag in soup.find_all("ul", class_="menu")[16].children:
        if tag.name == "li":
            event_data = tag.time["datetime"].split("T")[0]
            event_month = datetime.datetime.strptime(event_data, "%Y-%m-%d").month
            # фильтруем текущий и следующий месяц
            if event_month in (month_current, month_next):
                event.append((event_data, tag.a.string))

    return event


if __name__ == '__main__':
    hat = ["дата", "событие"]
    print(tabulate(main(), headers=hat, tablefmt='pipe'))

# docker run -ti --rm optk2k/parse
