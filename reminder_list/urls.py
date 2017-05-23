from django.conf.urls import url

from . import views

app_name = 'reminder_list'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^delete/(?P<question_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^clear$', views.clear, name='clear'),
    url(r'^edit/(?P<action>[a-z0-9]+)/$', views.edit, name='edit'),
    url(r'^successful_add$', views.successful_add, name='successful_add'),
    url(r'reminder_api', views.reminder_api, name='reminder api'),
]
