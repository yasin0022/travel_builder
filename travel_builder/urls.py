
from django.contrib import admin
from django.urls import path

from application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.create_customer,name='home'),
    path('create-customer/', views.create_customer, name='create_customer'),
    path('customer/detail/', views.customer_detail, name='customer_detail'),
    path('customer/profile/details/', views.customer_detail, name='profile'),
    path('customer/edit/', views.edit_customer, name='edit_customer'),
    path('destinations/create/', views.create_destination, name='create_destination'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/edit/<int:pk>/', views.edit_destination, name='edit_destination'),
    path('destinations/delete/<int:pk>/', views.delete_destination, name='delete_destination'),
    path('itineraries/new/', views.create_itinerary, name='create_itinerary'),
    path('destinations/<int:destination_id>/itineraries/', views.itineraries_by_destination, name='itineraries_by_destination'),
    path('itinerary/<int:itinerary_id>/activities/new/', views.create_activity, name='create_activity'),
    path('itineraries/<int:itinerary_id>/activities/', views.activities_by_itinerary, name='activities_by_itinerary'),
    path('activities/create/<int:itinerary_id>/', views.create_activity, name='create_activity'),
    path('activities/edit/<int:pk>/', views.edit_activity, name='edit_activity'),
    path('activities/delete/<int:pk>/',views.delete_activity, name='delete_activity'),
]
