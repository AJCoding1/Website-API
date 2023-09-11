from django.shortcuts import render
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import PostDocument
from rest_framework import permissions
from .serializers import PostElasticSearchSerializer



class PostElasticSearchView(DocumentViewSet):
    document = PostDocument
    serializer_class = PostElasticSearchSerializer
    lookup_field = 'id'
    permission_classes = [permissions.AllowAny]
    filter_backends = [

        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        SearchFilterBackend,
        DefaultOrderingFilterBackend

    ]

    search_fields = ('title','description','author','tags',)
    filter_fields = {"slug": "slug.raw", "tags": "tags", "created_at": "created_at"}

    ordering_fields = {'created_at':'created_at'}
    ordering = ('-created_at')


