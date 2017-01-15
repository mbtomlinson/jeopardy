from django.conf.urls import url
from . import views

app_name = 'jeopardy'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # ex: /jeopardy/5/
    url(r'^(?P<clue_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /jeopardy/5/results/
    url(r'^(?P<clue_id>[0-9]+)/result/$', views.result, name='result'),
    # ex: /jeopardy/5/answer/
    url(r'^(?P<clue_id>[0-9]+)/vote/$', views.answer, name='answer'),
    ]

