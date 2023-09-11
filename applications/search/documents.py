from django_elasticsearch_dsl import Document,fields
from applications.posts.models import Post

from django_elasticsearch_dsl.registries import registry




@registry.register_document
class PostDocument(Document):
    title = fields.TextField(attr='title')
    content = fields.TextField(attr='content')
    description = fields.TextField(attr='description')
    author = fields.TextField()
    tags = fields.KeywordField()

    class Index:
        name = 'posts'
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Post
        fields = ["created_at"]

    def prepare_author(self,instance):
        return f"{instance.author.first_name} {instance.author.last_name}"

    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]

