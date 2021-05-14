from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user':True,
}



urlpatterns = [
    path('coffees/', include('coffees.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(),name='login'),
]