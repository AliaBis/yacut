# Проект "Yacut"

### Сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.


![Yacut](https://github.com/AliaBis/yacut/blob/master/yacut.png)


## Используемые технологии:

***Python, FLask, SQLAlchemy, SQLite***

## Для запуска проекта:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone 
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

```
source venv/bin/activate
```

* Если у вас Windows

```
source venv/scripts/activate
```

Обновить и установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Добавить скрытый файл .env c настройками подключения базы данных.
Пример: 
```
FLASK_APP=yacut
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY='придумать свой ключ'
```

Запустить проект:

```
flask run
```

Применить миграции:

```
flask db upgrade
```

Проект будет доступен по адресу:

```
http://127.0.0.1:5000/
```

### Автор проекта:
Алия Бисенгалиева
