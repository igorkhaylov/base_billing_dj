<h1 align="center">django-template</h1>

## Project Setup
* [Python 3.12.2](https://www.python.org/downloads/release/python-3122/).
* [Virtuelenv](https://pypi.org/project/virtualenv/).

### requirements
<!-- * [django-stdimage](https://pypi.org/project/django-stdimage/) -->
<!-- * [django-ckeditor](https://pypi.org/project/django-ckeditor/) -->
* [Django](https://pypi.org/project/Django/)
* **main packages**
  * [Pillow](https://pypi.org/project/Pillow/)
  * [djangorestframework](https://pypi.org/project/djangorestframework/)
  * [django-rosetta](https://pypi.org/project/django-rosetta/)
  * [django-cors-headers](https://pypi.org/project/django-cors-headers/)
  * [django-admin-rangefilter](https://pypi.org/project/django-admin-rangefilter/)
  * [python-dateutil](https://pypi.org/project/python-dateutil/)
  * [drf-yasg](https://pypi.org/project/drf-yasg/)

* [django-filter](https://pypi.org/project/django-filter/)
* [celery[redis]](https://pypi.org/project/celery/)
* [pytils](https://pypi.org/project/pytils/)
* [autopep8](https://pypi.org/project/autopep8/)
* [pycodestyle](https://pypi.org/project/pycodestyle/)

### django-template
```shell
mkdir project_name
python -m virtualenv venv
source venv/bin/activate
pip install pillow django django-rosetta djangorestframework django-cors-headers python-dateutil
django-admin startproject config .
mkdir apps
cd apps
python ../manage.py startapp app_name
```

### generate compile locales
```shell
# generate locales
python manage.py makemessages -l ru -l en --ignore venv
# compile locales
python manage.py compilemessages
```

### generate secret key
``` python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
