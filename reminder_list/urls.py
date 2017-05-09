from django.conf.urls import url

from . import views

app_name = 'reminder_list'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_reminder, name='add reminder'),
    url(r'^successful_add$', views.successful_add, name='successful_add'),
]
