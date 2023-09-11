from django.db import models
from django.utils.translation import  gettext_lazy as trans
from django.contrib.auth import get_user_model
from applications.shares.models import ShareData
from applications.posts.models import Post

User = get_user_model()


class Bookmark(ShareData):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookmarks')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_bookmarks')

    def __Str__(self):
        return f"{self.post.title}"

    class Meta:
        verbose_name = trans('Bookmark')
        verbose_name_plural = trans('Bookmarks')
        unique_together = ["user", "post"]
        ordering = ["-created_at"]
