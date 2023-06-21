from django.urls import path  # для формирования маршрутов

from .views import *  # из car все наши представления

urlpatterns = [
    path('', CarsHome.as_view(), name='home'),
    path('about', about, name="about"),
    path('login/', LoginUser.as_view(), name='login'),
    path('contact', contact, name='contact'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CarsCategory.as_view(), name='category'),
    path('logout/', logout_user, name='logout'),
    path('favorites/', Favorites.as_view(), name='favorites'),
]
# Все маршруты текущего приложения
