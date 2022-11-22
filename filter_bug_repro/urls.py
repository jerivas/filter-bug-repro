"""filter_bug_repro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import models
from django.urls import include, path
from django_filters import rest_framework as filters
from rest_framework import routers, serializers, viewsets


class Document(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DocumentFilterSet(filters.FilterSet):
    class Meta:
        model = Document
        fields = ("owner",)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("id", "name", "owner")


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filterset_class = DocumentFilterSet


router = routers.DefaultRouter()
router.register(r"docs", DocumentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
