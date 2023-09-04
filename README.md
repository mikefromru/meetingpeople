# Meeting People
Веб приложение в котором реализованы REST API. Авторизованные пользователи просматривают фотографии профиля других участников, ставят лайки и если происходит взаимная симпатия отправлять письмо на email о взаимной симпатии. На каждой загруженной  пользователем аватарке устанавливается водяной знак данного приложения.
### Используемые технологии
- Python
- Django
- Django Rest Framework
- Docker

### Начать
1. Клонировать репозиторий
```
git clone 
https://github.com/mikefromru/meetingpeople.git
```
2. Перейти в папку проекта
```
cd /meetingpeople
```
3. Создать виртуальное окружение
```
python3.11 -m venv venv
```
4. Активировать виртуальное окружение
```
source venv/bin/activate
```
5. Установить зависимости
```
python install -r requirements.txt
```
6. Переименовать `backend/backend/.env.EXAMPLE` файл в `backend/backend/.env`

7. Запустить проект
```
python manage.py runserver
```
# Использование
- Получить список всех пользователей GET `http://0.0.0.0:8000/api/list`
- Поставить лайк пользователю POST `http:.0.0.0.0:8000/api/clients/like`
- Создать пользователя `http://0.0.0.0:8000:api/clients/create` 
