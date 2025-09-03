from django.contrib import admin
from .models import Point, Share


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "latitude", "longitude")
    search_fields = ("title",)
    list_per_page = 50


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "created_at", "points_count")
    search_fields = ("slug", "title")
    readonly_fields = ("slug", "created_at")
    filter_horizontal = ("points", )

    def points_count(self, obj):
        return obj.points.count()

    points_count.short_description = "Кол-во точек"
