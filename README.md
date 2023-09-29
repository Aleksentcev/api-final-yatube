![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

# API для проекта Yatube.

Проект API для социальной сети [Yatube](https://github.com/Aleksentcev/yatube-project.git).
Позволяет зарегистрироваться, создавать, редактировать и удалять собственные публикации, а так же читать публикации других пользователей и подписываться на них посредством API-запросов. Для неавторизованных пользователей API доступен только для чтения.

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

### Автор:

Михаил Алексенцев

[![Telegram](https://img.shields.io/badge/aleksentcev-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white&link=https://t.me/aleksentcev)](https://t.me/aleksentcev)
