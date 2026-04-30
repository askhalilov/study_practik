# Python + HTML/CSS animation demo

Готовый учебный пример: кнопка и индикатор загрузки анимируются через HTML/CSS, а состояние анимации синхронизируется с событием Python — загрузкой файла во Flask.

## Что внутри

- `app.py` — Flask-приложение с маршрутом `/upload`.
- `templates/index.html` — интерфейс, CSS-анимации и JavaScript-синхронизация.
- `tests/test_app.py` — базовые тесты для GitHub Actions.
- `.github/workflows/python-ci.yml` — workflow для проверки проекта на GitHub Actions.
- `requirements.txt` — зависимости проекта.
- `.gitignore` — исключения для Git.

## Локальный запуск

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

### Установка и запуск

```bash
pip install -r requirements.txt
python app.py
```

Откройте в браузере:

```text
http://127.0.0.1:5000
```

## Проверка тестов локально

```bash
pytest -q
```

## Как запушить на GitHub

Создайте пустой репозиторий на GitHub, затем в папке проекта выполните:

```bash
git init
git add .
git commit -m "Initial Flask animation demo"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

После пуша GitHub Actions автоматически запустит workflow из файла:

```text
.github/workflows/python-ci.yml
```

Посмотреть результат можно во вкладке **Actions** вашего репозитория.

## Как работает синхронизация

1. Пользователь выбирает файл и нажимает кнопку.
2. JavaScript включает CSS-классы `loading` и `active`.
3. Запрос отправляется в Python Flask на `/upload`.
4. Flask сохраняет файл и возвращает JSON-ответ.
5. JavaScript получает ответ и выключает анимацию.

