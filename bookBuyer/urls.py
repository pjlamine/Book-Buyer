from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "bookBuyer"
urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^isbn$',  views.isbn, name='isbn'),
     url(r'^retrievePrice$',  views.retrievePrice, name='getPrice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
