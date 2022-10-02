from datetime import datetime
import requests


def function_tuning(any_function):

    def tuned_function(*args, **kwargs):
        date_data = (datetime.today())
        function_name = any_function.__name__
        pikus = any_function(*args, **kwargs)
        with open('information_data.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата запуска <<{function_name}>> функции <<{date_data}>>\n,'
                       f'аргументы: {args}_{kwargs}, значение: {pikus}')
        return pikus

    return tuned_function


def pok():
    res = requests.get(url, headers = headers).text
