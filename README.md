### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Aleksentcev/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API:

Запрос:

```
GET .../api/v1/posts/
```

Ответ:

```
{
    "id": 1,
    "author": "admin",
    "text": "Тестовый пост",
    "pub_date": "2023-03-30T09:42:03.423395Z",
    "image": null,
    "group": 1
},
{
    "id": 2,
    "author": "admin",
    "text": "Тестовый пост 2",
    "pub_date": "2023-03-30T09:42:17.930555Z",
    "image": null,
    "group": null
}
```

Запрос:

```
POST .../api/v1/follow/

{
    "following": "admin2"
}
```

Ответ:

```
{
    "id": 1,
    "user": "admin",
    "following": "admin2"
}
```

Запрос:

```
PATCH .../api/v1/posts/1/

{
    "text": "Тестовый измененный текст"
}
```

Ответ:

```
{
    "id": 1,
    "author": "admin",
    "text": "Тестовый измененный текст",
    "pub_date": "2023-03-30T09:42:03.423395Z",
    "image": null,
    "group": 1
}
```