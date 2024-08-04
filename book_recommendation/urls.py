from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("apis/", include("book_recommendation.api_urls"))
]
