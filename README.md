# Yatube API
REST API для проекта Yatube

## Описание
Yatube API — это REST API для социальной платформы, где пользователи могут публиковать посты, 
комментировать их, объединяться в сообщества и подписываться друг на друга.

API предоставляет:
- управление публикациями (CRUD),
- работу с комментариями,
- получение списка сообществ,
- механизм подписок на авторов,
- JWT-аутентификацию.

## Технологии
- Python 3.x
- Django
- Django REST Framework
- Simple JWT
- SQLite
- OpenAPI (Swagger)

## Установка и запуск проекта
1. Клонировать репозиторий и перейти в него в командной строке:
```shell
git clone https://github.com/bobridze5/api-final-yatube-ad
```

```shell
cd api-final-yatube-ad
```

2. Cоздать и активировать виртуальное окружение:
```shell
python3 -m venv env
```
```shell
source env/bin/activate
```

3. Установить зависимости из файла requirements.txt:
```shell
python3 -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```

4. Перейти в директорию проекта и выполнить миграции:
```shell
cd yatube_api
```
```shell
python3 manage.py migrate
```

5. Запустить проект:
```shell
python3 manage.py runserver
```

## Пример запроса
Запрос:
```shell
GET /api/v1/posts/?limit=10&offset=0
```

Ответ:
```json
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/v1/posts/?offset=10&limit=10",
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": "user",
      "text": "Текст публикации",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": null,
      "group": 1
    }
  ]
}
```

> [!NOTE]  
> 
> Подробнее с API можно ознакомиться в файле ``static/redoc.yaml``