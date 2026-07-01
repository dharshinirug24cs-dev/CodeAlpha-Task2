from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_event, name='register_event'),
    path('registrations/', views.registration_list, name='registration_list'),
    path('registrations/<int:registration_id>/cancel/', views.cancel_registration, name='cancel_registration'),
    path('api/events/', views.api_event_list, name='api_event_list'),
    path('api/events/<int:event_id>/', views.api_event_detail, name='api_event_detail'),
    path('api/registrations/', views.api_registration_list, name='api_registration_list'),
]