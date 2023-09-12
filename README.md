## BOOK_API - Коллекция книг

### Возможности проекта:
- Доступ к просмотру книг, ссылка на скачивание книги(разрешено всем пользователям)
- Добавлять, удалять или изменять книги разрешено только администратору
- Регистрация по токену(при запуске проекта создаётся администратор)


### Используемые технологии:
- Python 3.11
- fastapi 0.103.0
- uvicorn
- sqlalchemy 2.0.20
- alembic 1.12.0
- fastapi-users 12.1.2

### Установка:
#### 1: Клонируйте репозиторий:
```
git clone git@github.com:SkaDin/api_bookstore.git
```
#### 2: Установите зависимости и активируйте виртуальное окружение:
```commandline
poetry install

poetry shell
```
#### 3: Создайте и примените миграции БД:
```commandline
alembic revision --autogenerate
alembic upgrade head 
```
#### 4. Пример .env-файла
```
APP_TITLE='Книжный магазин'
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=ChokoPie
FIRST_SUPERUSER_EMAIL=ex.exam@ple.com
FIRST_SUPERUSER_PASSWORD=123456789
```
### Aвтор: SkaDin(Сушков Денис)
