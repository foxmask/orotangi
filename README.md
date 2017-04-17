Orotangi
========

Your Thoughts, Everywhere 


Requirements
------------

The minimum are the following :

* Python 3.6.x
* [Django Rest Framework](http://www.django-rest-framework.org/) == 3.6.2
* [Django](https://www.djangoproject.com/) 1.11
* [django-cors-headers](https://pypi.python.org/pypi/django-cors-headers) == 2.0.2
* [django-filter](https://pypi.python.org/pypi/django-filter) == 1.0.2


Installation
------------

```bash
python3.6 -m venv orotangi
cd $_
git clone http://github.com/foxmask/orotangi
pip install -r requirements.txt
cd orotangi
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver localhost:8001
```

Data Sample
-----------

after logged in from http://localhost:8001/

* to add some books go to http://localhost:8001/api/orotangi/books/

