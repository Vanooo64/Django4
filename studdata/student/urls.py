from django.urls import path, re_path, register_converter
from . import views
from . import converters # імпортуемо файл з конверторами

register_converter(converters.FourDigitYearConverter, "year4") # функція register_converter дозволяє зареструвати новий конвертер

urlpatterns = [
    path('', views.index),
    path('cats/<int:cat_id>/', views.categories),  # <int:cat_id> - дозволить підставляти динамічний ID у вигляді цифр
    path('cats/<slug:cat_slug>/', views.categories_by_slug), # <slug:cat_slug> - дозволить підставляти динамічний ID у вигляді цифр, букв і тере
    path("archive/<year4:year>/", views.archive), #
]