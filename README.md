# generator_service

Текст [задания](task.md).

Сервис вывода значений на заданное число, промежуток или список чисел в диапазоне от 1 до 1000.

## Установка

- Установите зависимости:
```bash
pip install -r requirements.txt
```


## Запуск сервиса

```bash
uvicorn src.main:app --reload
```

## Клиент для работы с API

1. Пример для отправки 1 числа:
```bash
python3 api_client.py -n 6
```

2. Пример для отправки списка:
```bash
python3 api_client.py -a 3 5 7 9
```

3. Пример для отправки промежутка(минимальное и максимальное значение):
```bash
python3 api_client.py -r 3 5
```

4. Для получения помощи по аргументам:
```bash
python3 api_client.py -h
```

## Клиент для работы с websocket

1. Пример для отправки 1 числа:
```bash
python3 ws_client.py -n 6
```

2. Пример для отправки списка:
```bash
python3 ws_client.py -a 3 5 7 9
```

3. Пример для отправки промежутка(минимальное и максимальное значение):
```bash
python3 ws_client.py -r 3 5
```

4. Для получения помощи по аргументам:
```bash
python3 ws_client.py -h
```
