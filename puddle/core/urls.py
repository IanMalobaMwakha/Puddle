from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    path('profile_not_found/', views.profile_not_found, name='profile_not_found'),
    path('faq/', views.faq, name='faq'),
    path('product_listing_policy/', views.product_listing_policy, name='product_listing_policy'),
    path('signup/', views.signup, name='signup'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form = LoginForm), name='login'),
]

