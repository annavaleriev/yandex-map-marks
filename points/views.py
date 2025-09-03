from rest_framework import viewsets, mixins
from .models import Share
from .serializers import ShareSerializer
from django.shortcuts import get_object_or_404, render


class ShareViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):

    queryset = Share.objects.all().order_by("-created_at")
    serializer_class = ShareSerializer
    lookup_field = "slug"


def map_page_slug(request, slug: str):
    """
    Страница карты для конкретного Share.
    """
    get_object_or_404(Share, slug=slug)
    return render(request, "points/map_share.html", {"slug": slug})


def map_edit_page(request):
    return render(request, "points/map_edit.html")
