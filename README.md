# Тестовое задание для "Онлайн-школа Тетрика"

## Установка 
Клонирование репозитория
```zsh
git clone https://github.com/NikitaKrylov/TetrikaTestTasks.git # скачивание репозитория
cd TetrikaTestTasks # переход в папку
```

Создание окружения и установка пакетов(для unix)
```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Запуск тестов
```zsh
# Тесты для задания 1 
pytest task1/solution/tests.py

# Тесты для задания 2
pytest task2/solution/tests.py

# Тесты для задания 3 
pytest task3/solution/tests.py
```