# My Django Shop

Это проект на Django, который использует Stripe API для обработки платежей. В проекте реализованы модели для товаров, заказов, скидок и налогов.

## Установка

### Предварительные требования

- Python 3.8 или выше
- pip
- Docker (опционально, если вы хотите использовать контейнеризацию)

### Клонирование репозитория

Сначала клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Установка зависимостей

Если вы не используете Docker, установите зависимости с помощью pip:

```bash
pip install -r requirements.txt
```

### Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта и добавьте ваши ключи Stripe:

STRIPE_SECRET_KEY=your_stripe_secret_key

STRIPE_PUBLIC_KEY=your_stripe_public_key

SECRET_KEY='SECRET_KEY'

DEBUG=True

ALLOWED_HOSTS="*"

### Миграция базы данных

Примените миграции для создания необходимых таблиц в базе данных:

```bash
python manage.py makemigrations
python manage.py migrate
```



### Заполнение базы данных (опционально)

Если вы хотите заполнить базу данных тестовыми данными, вы можете создать скрипт или использовать Django Admin для добавления товаров.

### Запуск сервера

Запустите сервер разработки:

```bash
python manage.py runserver
```

Теперь вы можете открыть браузер и перейти по адресу [http://localhost:8000](http://localhost:8000).

## Использование Docker (опционально)

Если вы хотите запустить проект с помощью Docker, выполните следующие шаги:

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Запустите проект с помощью Docker Compose:
```bash
docker-compose up --build
```


Теперь вы можете открыть браузер и перейти по адресу [http://localhost:8000](http://localhost:8000).

## Структура проекта
```bash
myproject/
│
├── shop/ # Приложение для работы с товарами
│ ├── migrations/ # Папка для миграций базы данных
│ ├── init.py
│ ├── admin.py # Настройки админки
│ ├── apps.py # Конфигурация приложения
│ ├── models.py # Модели данных
│ ├── tests.py # Тесты
│ ├── views.py # Представления
│ ├── urls.py # URL-адреса приложения
│ └── templates/ # Шаблоны HTML
│ ├── item_detail.html # Шаблон для отображения товара
│ └── item_list.html # Шаблон для списка товаров
│
├── myproject/ # Основная папка проекта
│ ├── init.py
│ ├── settings.py # Настройки проекта
│ ├── urls.py # Основные URL-адреса проекта
│ └── wsgi.py # WSGI конфигурация
│
├── Dockerfile # Dockerfile для контейнеризации
├── docker-compose.yml # Файл для настройки Docker Compose
├── manage.py # Скрипт для управления проектом
└── requirements.txt # Зависимости проекта
```


## Лицензия

Этот проект лицензирован под MIT License - смотрите файл [LICENSE](LICENSE) для подробностей.

## Контакты

Если у вас есть вопросы или предложения, не стесняйтесь обращаться ко мне по адресу [yagofarov.vadim@mail.ru].


