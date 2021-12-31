from django.urls import path
from . import views


urlpatterns = [
	path('', views.index), # our-domain.com/
	path('post/<slug:post_id>', views.post_details) # our-domain.com/<dynamic>
]