from django.urls import path
from .views import HomeView, LoginView, BaseView, NewForm, RenewView
app_name = 'App'
urlpatterns = [
    path('', HomeView.as_view(), name="Home"),
    path('login/', LoginView.as_view(), name="Login"),
    path('base/', BaseView.as_view(), name="Base"),
    path('new-license/', NewForm.as_view(), name="New"),
    path('renew/', RenewView.as_view(), name="Renew"),
]