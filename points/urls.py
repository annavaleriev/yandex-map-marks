from django.urls import path
from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from .views import ShareViewSet, map_page_slug, map_edit_page

router = DefaultRouter()
router.register("shares", ShareViewSet, basename="shares")

urlpatterns = [
    path("map/", lambda r: render(r, "points/map_root.html"), name="map-root"),
    path("map/edit/", map_edit_page, name="map_edit_page"),
    path("map/<slug:slug>/", map_page_slug, name="map_page_slug"),
] + router.urls
