from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books import views

router = DefaultRouter()

router.register("book", views.BooksViewset, basename="books-apis")

urlpatterns = [

]+router.urls
