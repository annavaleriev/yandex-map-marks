from rest_framework import serializers
from .models import Point, Share


class PointSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Point (чтение).
    """
    class Meta:
        model = Point
        fields = ("id", "title", "latitude", "longitude")


class PointCreateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для создания точки.
    """
    class Meta:
        model = Point
        fields = ("latitude", "longitude")


class ShareSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Share (подборка точек).
    """
    points = PointCreateSerializer(many=True)

    def create(self, validated_data):
        # сделать оптимизацию через bulk_create
        points = validated_data.pop("points")
        share_points = []
        if points:
            for point in points:
                point, _ = Point.objects.get_or_create(latitude=point["latitude"], longitude=point["longitude"])
                share_points.append(point)
        share = super().create(validated_data)
        share.points.set(share_points)
        return share

    class Meta:
        model = Share
        fields = ("id", "slug", "created_at", "points")
        read_only_fields = ("id", "slug", "created_at")
