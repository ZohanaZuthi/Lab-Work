from django.contrib import admin
from django.urls import path
from booking.views import home, hotels, book

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('hotels/', hotels),
    path('book/', book),
]
