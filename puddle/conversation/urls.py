from django import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<item_pk>/', views.new_conversation, name='new'),
]