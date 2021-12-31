from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='all-posts'), # our-domain.com/
	path('post/<slug:post_id>', views.post_details, name='post-detail') # our-domain.com/<dynamic>
]