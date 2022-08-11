# Урок 18. Архитектура. Домашнее задание

В этом задании вам нужно будет написать проект для онлайн-кинотеатра, разложив его по папочкам. **Предлагаем оценить свои силы и выбрать версию с плоской архитектурой (попроще) или слоеную архитектуру MVC (посложнее).**

БД:

[movies.db](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65b5f76e-65ca-4018-b41a-cfdd3765dcf3/movies.db)

# Простая версия

### Шаг 1. Используйте репозиторий с архитектурой проекта

Скопируйте структуру из репозитория (https://github.com/skypro-008/flask-easy-blank).

Установите зависимости и убедитесь, что всё работает. 

Теперь вы готовы писать проект!

### Шаг 2. Создайте представления

Используя Flask-RESTX, создайте три неймспейса и отдельные папки под них.  Так, чтобы вьюхи для каждого неймспейса оказались в своей папке.

Пропишите соответствующие методы.

**Для фильмов:**

- [ ]  GET /movies — получить все фильмы.
- [ ]  GET /movies/3 — получить фильм по ID.
- [ ]  GET /movies?director_id=15 — получить все фильмы режиссера.
- [ ]  GET /movies?genre_id=3 — получить все фильмы жанра.
- [ ]  GET /movies?year=2007 — получить все фильмы за год.
- [ ]  POST /movies — создать фильм.
- [ ]  PUT /movies/1 — изменить информацию о фильме.
- [ ]  DELETE /movies — удалить фильм.

**Для режиссеров:**

- [ ]  GET /directors — получить всех режиссеров.
- [ ]  GET /directors/3 — получить режиссера по ID.

**Для жанров:**

- [ ]  GET /genres — получить все жанры.
- [ ]  GET /genres/3 — получить жанр по ID.

Создайте Class-Based Views и напишите методы, которые возвращали бы пустые строки. Запустите приложение и, используя Postman, убедитесь, что всё работает.

### Шаг 3. Создайте модели

**Фильм** (Movie)

id

title

description

trailer

year

rating

genre_id (связь с Genre)

director_id (связь с Director)

**Жанр** (Genre)

id

name

**Режиссер** (Director)

id

name

### Шаг 4. Напишите схемы сериализации

Напишите схемы сериализации для Movie, Genre, Director и разместите их в models.py.

### Шаг 5. Допишите код вьюшек — жанры

Внутри соответствующего файла в папке views допишите представления:

- [ ]  GET /genres — получить все жанры.
- [ ]  GET /genres/3 — получить жанр по ID.

### Шаг 6. Допишите код вьюшек — режиссеры

Внутри соответствующего файла в папке views допишите представления:

 

- [ ]  GET /directors — получить всех режиссеров.
- [ ]  GET /directors/3 — получить режиссера по ID.

### Шаг 7. Допишите код вьюшек — фильмы

Внутри соответствующего файла в папке views допишите представления:

- [ ]  GET /movies — получить все фильмы.
- [ ]  GET /movies/3 — получить фильм по ID.
- [ ]  GET /movies?director_id=15 — получить все фильмы режиссера.
- [ ]  GET /movies?genre_id=3 — получить все фильмы жанра.
- [ ]  GET /movies?year=2007 — получить все фильмы за год.
- [ ]  POST /movies — создать фильм.
- [ ]  PUT /movies/1 — изменить информацию о фильме.
- [ ]  DELETE /movies — удалить фильм.

### Шаг 8. Убедитесь, что всё работает!

Надеемся, всё это время вы делали атомарные коммиты в ветку develop. Теперь, когда всё приложение готово, отправьте pull request в главную ветку и сдайте задание на проверку.

### Критерии приема простой версии

- :white_check_mark:  Модели описаны корректно, данные заполнены.
- :white_check_mark:  Схемы описаны корректно — сериализация работает.
- :white_check_mark:  Статус-коды верные.
- :white_check_mark:  Фильтры работают.
- :white_check_mark:  Ответы на GET-запросы верные.
- :white_check_mark:  Заголовок Location есть в POST на создание сущности.
- :white_check_mark:  Неймспейсы зарегистрированы верно, файлы с CBV лежат в верных местах.

---

---

# Часть 2. Сложная версия

### Шаг 1. Используйте репозиторий с архитектурой проекта

Скопируйте структуру и заготовки из репозитория заготовки (https://github.com/skypro-008/flask-hard-blank).

Установите зависимости и убедитесь, что всё работает. Теперь вы готовы писать проект!

### Шаг 2. Создайте представления

Используя Flask-RESTX, создайте три неймспейса и отдельные папки под них. Пропишите соответствующие методы.

**Для фильмов**

- [ ]  Получение по id
- [ ]  Получение всех
- [ ]  Добавление
- [ ]  Изменение
- [ ]  Удаление

**Для режиссеров**

- [ ]  Получение по id
- [ ]  Получение всех

**Для жанров**

- [ ]  Получение по id
- [ ]  Получение всех

Создайте Class-Based Views и напишите методы, которые возвращали бы пустые строки или какие-то рандомные данные. Запустите приложение и, используя Postman, убедитесь, что всё работает.

### Шаг 3. Создайте модели

**Фильм** (Movie)

- [ ]  id
- [ ]  title
- [ ]  description
- [ ]  trailer
- [ ]  year
- [ ]  rating
- [ ]  genre_id (связь с Genre)
- [ ]  director_id (связь с Director)

**Жанр** (Genre)

- [ ]  id
- [ ]  name

**Режиссер** (Director)

- [ ]  id
- [ ]  name

### Шаг 3.1. Наполните БД

Создайте объекты фильмов, жанров и режиссеров и сохраните их в БД.

**Или** в приложении для работы с БД (например, DBeaver) или в плагине к PyCharm для работы с БД создайте строки в таблице — наполните БД.

### Шаг 4. Напишите схемы сериализации

Напишите схемы сериализации для Movie, Genre, Director и разместите их там, где предусмотрено архитектурой. 

### Шаг 5. Напишите DAO

Напишите объекты доступа к данным для трех моделей.

**Фильм** (Movie)

- [ ]  Получить все фильмы
- [ ]  Получить фильм по id
- [ ]  Получить все фильмы режиссера
- [ ]  Получить все фильмы жанра
- [ ]  Получить все фильмы за год
- [ ]  Создать фильм
- [ ]  Изменить информацию о фильме
- [ ]  Удалить фильм

**Режиссер** (Director)

- [ ]  Получить всех режиссеров
- [ ]  Получить по id

**Жанр** (Genre)

- [ ]  Получить все жанры
- [ ]  Получить по id

### Шаг 6. Напишите сервисы

Теперь, когда все методы работы с данными подготовлены, пора браться за бизнес-логику. Напишите код для трех сервисов, используя DAO.

**Для фильмов**

- [ ]  Добавление фильма
- [ ]  Получение фильма
- [ ]  Получение всех фильмов
- [ ]  Изменение фильма
- [ ]  Фильтрация фильма по разным полям
- [ ]  Удаление фильма

**Для режиссеров**

- [ ]  Получение всех
- [ ]  Получение по id

**Для жанров**

- [ ]  Получение всех
- [ ]  Получение по id

### Шаг 7. Допишите код **views** с использованием сервисов

**Допишите код views жанров:**

- [ ]  GET /genres — получить все жанры.
- [ ]  GET /genres/3 — получить жанр по ID.

**Допишите код views режиссеров:**

- [ ]  GET /directors — получить всех режиссеров.
- [ ]  GET /directors/3 — получить режиссера по ID.

**Допишите код views фильмов:**

- [ ]  GET /movies — получить все фильмы.
- [ ]  GET /movies/3 — получить фильм по ID.
- [ ]  GET /movies?director_id=15 — получить все фильмы режиссера.
- [ ]  GET /movies?genre_id=3 — получить все фильмы жанра.
- [ ]  GET /movies?year=2007 — получить все фильмы за год.
- [ ]  POST /movies — создать фильм.
- [ ]  PUT /movies/1 — изменить информацию о фильме.
- [ ]  DELETE /movies/1 — удалить фильм.

### Критерии приема сложной версии

- :white_check_mark:  Модели описаны корректно, данные заполнены.
- :white_check_mark:  Схемы описаны корректно — сериализация работает .
- :white_check_mark:  Статус-коды верные.
- :white_check_mark:  Фильтры работают.
- :white_check_mark:  Ответы на GET-запросы верные.
- :white_check_mark:  Заголовок Location есть в POST на создание сущности.
- :white_check_mark:  Неймспейсы зарегистрированы верно, файлы с CBV лежат в верных местах.
- :white_check_mark:  DAO-слой описан корректно.
- :white_check_mark:  Нет циклических импортов.
