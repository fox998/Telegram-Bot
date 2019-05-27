
import requests
from urllib import parse
from bs4 import BeautifulSoup
from markdownify import markdownify as md


identifier_of_time_section = {'style': 'font-size: 12px; text-align: center'}
identifier_of_current_day_section = {'class': 'yellow'}


def formating_lesson_data(lesson_data):
    md_data = md(lesson_data)
    return md_data[0:md_data.find('(')]


def parse_timetable(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')

    lesson_data = [formating_lesson_data(val) for val in soup.find_all('td', identifier_of_current_day_section)]
    time_set = {md(val) for val in soup.find_all('div', identifier_of_time_section)}

    return [f'\t\n{time} {data}\n' for (time, data) in zip([*sorted(time_set)][0::2], lesson_data)]


def today_timetable(groupe):

    http_response = requests.get('https://rozklad.org.ua/timetable/group/' + parse.quote(groupe))
    responce = 'Can`t find the groupe'

    if http_response.status_code == 200:
        responce = ''
        for lesson in parse_timetable(http_response.text):
            responce += lesson

    return responce


if __name__ == "__main__":
    print(today_timetable('тк-71'))
