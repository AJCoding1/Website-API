from django.db import models
from applications.shares.models import ShareData
from django.utils.translation import gettext_lazy as trans
from django.contrib.auth import get_user_model
from applications.posts.models import Post

User = get_user_model()


class Rating(ShareData):
    RATING_CHOICES = [
        (1,trans('Very Poor')),
        (2,trans('Poor')),
        (3,trans('Neutral')),
        (4,trans('Good')),
        (5,trans('Excellent'))
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    review = models.TextField(verbose_name=trans('Review'), blank=True, null=True)
    rating = models.PositiveIntegerField(verbose_name=trans('Rating'), choices=RATING_CHOICES)


    def __str__(self):
        return f'{self.post.title} is rated by {self.user.first_name}'

    class Meta:
        unique_together = ['post','user']
        verbose_name = trans('Rating')
        verbose_name_plural = trans('Ratings')
