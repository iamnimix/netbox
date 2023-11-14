## How to use

1. create python env and activate
   - `python -m venv venv`
   - `source venv/bin/activate`
2. install requirements
   - `pip install -r requirements.txt`
3. run `python manage.py makemigrations movie && python manage.py migrate`
4. `scrapy crawl movies`
5. runserver `python manage.py runserver`