from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import PostDocument


class PostElasticSearchSerializer(DocumentSerializer):
    class Meta:
        document = PostDocument
        fields = ['title','description','content','author','created_at']