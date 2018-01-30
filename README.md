#Blog.me
## О программе
Простой блог на Django

![alt text](http://preview.ibb.co/b6UsPR/Screen_Shot_2018_01_30_at_21_35_58.png)

## Необходимое ПО и библиотеки:
1. Python 3.6
2. Django 2.0
3. PostgreSQL

## Установка:
1. Копируем репозиторий:
```bash
git clone https://github.com/MrJackJones/Blog.me.git
```

2. Подготавливаем базу:
```bash
python3.6 manage.py makemigrations
python3.6 manage.py migrate
```

3. Создаем главного администратора:
```bash
python3.6 manage.py createsuperuser
```

4. Запускаем сервер
```bash
python3.6 manage.py runserver
```
5. Открываем в браузере
```bash
http://127.0.0.1:8000/
```