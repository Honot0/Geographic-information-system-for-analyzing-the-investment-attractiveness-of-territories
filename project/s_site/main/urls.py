# pip install django
#
# django-admin startproject s_site
#
# python manage.py startapp s2_site
#
# python manage.py runserver
# python3 manage.py runserver 193.122.59.88:8000

# python manage.py migrate
# python manage.py createsuperuser


from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [

    path('', views.mainPage, name = "home"),
    path('map', views.mapPage, name = "map")
    # url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True))
]
