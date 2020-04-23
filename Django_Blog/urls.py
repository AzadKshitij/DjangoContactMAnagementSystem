from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
urlpatterns = [
    path('creator/', admin.site.urls),
    path('', include('ContactManagement.urls')),
    path('register/', user_views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='user-logout'),
    path('profile/', user_views.profile, name='user-profile'),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
