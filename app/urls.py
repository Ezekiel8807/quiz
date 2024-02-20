from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('addquiz/', views.addquiz, name='addquiz'),
    path('quiz/submitquiz/', views.submitquiz, name='submitquiz'),
    path('addquiz/createquiz/', views.createquiz, name='createquiz'),
    
]
