from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

from applications.posts.models import Post


@receiver(post_save, sender=Post)
def update_document(sender, instance=None, created=False, **kwargs):
    """Update the PostDocument in Elasticsearch when an post instance is updated or created"""
    registry.update(instance)


@receiver(post_delete, sender=Post)
def delete_document(sender, instance=None, **kwargs):
    """Delete the PostDocument in Elasticsearch when a post instance is deleted"""
    registry.delete(instance)
