from django.urls import path
from .import views
urlpatterns = [
    path('', views.register, name='register'),
    path("donor_search/",views.donor_search, name="donor_search"),
    path('donor_list/', views.donor_list, name='donor_list'),
]   
