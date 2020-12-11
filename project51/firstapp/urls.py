from django.urls import path 
from firstapp import views 

urlpatterns = [
				path('welcome/', views.home_page),
				path('physics/', views.display_physics_information),
				path('chemistry/', views.display_chemistry_information),
				path('social/', views.display_social_information),
]