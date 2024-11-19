from pathlib import Path

from task2.solution.solution import parce_beasts, get_beasts_count, write_file


def test_parce_beasts_file_exists():
    path = Path('beasts.csv')

    # Проверка, что список элементов не пустой
    items = get_beasts_count(url='https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту')
    assert len(items)

    # Проверка существования целевого файла
    write_file(filename=str(path), items=items)
    assert path.exists(), f'File {path} not found.'
