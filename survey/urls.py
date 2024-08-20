# survey/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('survey/<int:pk>/', views.survey_detail, name='survey_detail'),
    path('', views.home, name='home'),
    path('create/', views.create_survey, name='create_survey'),  # اطمینان از اینکه این خط وجود دارد
]
