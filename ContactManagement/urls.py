from django.urls import path
from .views import (
    ContactListView,
    UserContactListView,
    ContactDetailView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView
)
from . import views

urlpatterns = [
    path('', ContactListView.as_view(), name='contact-home'),
    path('user/<str:username>', UserContactListView.as_view(), name='user-contact'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/',
         ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/',
         ContactDeleteView.as_view(), name='contact-delete'),
    path('about/', views.about, name='contact-about'),
]
