# Meeting People
Веб приложение в котором реализованы REST API. Авторизованные пользователи просматривают фотографии профиля других участников, ставят лайки и если происходит взаимная симпатия отправлять письмо на email о взаимной симпатии.
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
```
7. Запустить проект
```
python manage.py runserver
```
#Использование

