from django.urls import path
from . import views


urlpatterns = [
	path('board/', views.index) # our-domain.com/board
]