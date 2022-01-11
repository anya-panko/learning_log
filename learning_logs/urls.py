"""defines URL schemes for learning_logs"""

from django.urls import path
from . import views
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page with the whole themes
    path('topics/', views.topics, name='topics'),
    # page with the information on a separate topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
