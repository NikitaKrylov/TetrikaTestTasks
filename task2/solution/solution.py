import csv
from collections import defaultdict
import requests
from bs4 import BeautifulSoup


def get_beasts_count(url: str, items: defaultdict | None = None) -> defaultdict:
    """Рекурсивный сбор элементов"""
    if not items:
        items = defaultdict(int)

    print(f"Process page: {url}")
    response = requests.get(url)
    assert response.ok
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    url = soup.find_all('a', title="Категория:Животные по алфавиту")[-1].attrs.get('href', None)

    groups = soup.find_all('div', class_='mw-category-group')

    for group in groups:
        if (tag := group.find('h3').text) is None:
            continue

        # Проверяем, что поиск идет по русским буквам
        if not ('А' <= tag.upper() <= 'Я'):
            return items

        links = group.find_all('a')
        items[tag] += len(links)
    print(items)

    return get_beasts_count(f'https://ru.wikipedia.org{url}', items=items)


def write_file(items: dict, filename: str) -> None:
    """Запись элементов словаря в файл по ключу и значению"""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Буква алфавита', 'Количество'])

        # Записываем данные в CSV, сортируем по алфавиту
        for letter in sorted(items.keys()):
            count = items[letter]
            writer.writerow([letter, count])
            print(f"{letter}: {count}")


def parce_beasts(filename: str = 'beasts.csv') -> None:
    """Главная фцнкция вызова парсера"""
    items = get_beasts_count(url='https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')
    write_file(items, filename)
