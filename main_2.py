from datetime import datetime
from bs4 import BeautifulSoup
import requests

file_name = 'information_data.txt'


def func_tun_path(path):

    def function_tuning(any_function):

        def tuned_function(*args, **kwargs):
            date_data = (datetime.today())
            function_name = any_function.__name__
            pikus = any_function(*args, **kwargs)
            with open('information_data_2.txt', 'w', encoding='utf-8') as file:
                file.write(f'Дата запуска <<{function_name}>> функции <<{date_data}>>\n,'
                           f'аргументы: {args}_{kwargs}, значение: {pikus}')
            return pikus
        return tuned_function
    return function_tuning


@func_tun_path(file_name)
def articl_data(x):  # x это страница на habr
    main_url = 'https://habr.com'
    url = main_url + f'/ru/all/page{x}/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, features='html.parser')

    articl_inf = []
    news_articles = soup.find_all('article')
    for news_article in news_articles:
        last_title = news_article.find("a", class_="tm-article-snippet__title-link").text
        articl_inf.append(last_title)
    return articl_inf


if __name__ == '__main__':
    articl_data(1)
