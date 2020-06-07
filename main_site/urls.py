from django.urls import path

from .views.home import IndexView
from .views.accounts import RegisterView, LoginView, LogoutView
from .views.shop import ShopCreateView, ShopView, BookView, BookingsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('shop', ShopView.as_view(), name='shop'),
    path('bookings', BookingsView.as_view(), name='bookings'),
    path('book/<int:pid>', BookView.as_view(), name='book'),
    path('create', ShopCreateView.as_view(), name='create'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
]