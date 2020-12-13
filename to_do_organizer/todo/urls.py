from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlist", views.createlist, name="createlist"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("add/<int:id>", views.add, name="add"),
    path("updatestatus", views.updatestatus, name="updatestatus"),
    path("filter/<str:filter>/<int:id>", views.filter, name="filter"),
    path("order/<str:ordering>/<int:id>", views.order, name="order"),
]