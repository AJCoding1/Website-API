from django.db import models
from django.utils.translation import gettext_lazy as trans
from applications.shares.models import ShareData
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

User = get_user_model()



class PostLike(ShareData):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
   


    def __str__(self):
        return f"{self.user.first_name}' likes"

    class Meta:
        unique_together = ["user", "post"]
        ordering = ["-created_at"]



class Post(ShareData):
    title = models.CharField(verbose_name=trans('Title'), max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    photo = models.ImageField(verbose_name=trans('Post Photo'), default='default.png')
    content = models.TextField(verbose_name=trans('Content'))
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    description = models.CharField(verbose_name=trans("description"), max_length=255)
    status = models.BooleanField(verbose_name=trans('Status'),default=True)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, through='PostLike', related_name='likes')


    def __str__(self):
        return f'{self.title}'

    @property
    def post_view_count(self):
        return self.post_views.count()


    @property
    def reading_time(self):
        title = self.title
        description = self.description
        content = self.content
        total_word = title + description + content
        total_word_count = len(total_word.split(' '))
        time = total_word_count/250
        return time

    @property
    def average_rating(self):
        total_rate = 0
        for rate in self.ratings.all():
            total_rate += rate.rating

            average = (total_rate/self.ratings.all().count())
        return round(average,2)



    class Meta:
        verbose_name = trans('Post')
        verbose_name_plural = trans('Posts')

    




class PostView(ShareData):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_views"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_views', null=True)
    ip = models.GenericIPAddressField(verbose_name='IP Address', null=True, blank=True)


    def __str__(self):
        return f"{self.post.title} viewed by {self.user.first_name if self.user else 'Anonymous'} from IP {self.ip}"

    class Meta:
        verbose_name = trans('Post View')
        verbose_name_plural = trans('Post Views')
        unique_together = ["user", "post"]

    @classmethod
    def save_post_view(cls,user,post,ip):
        view,_ = cls.objects.get_or_create(user=user, post=post, ip=ip)
        view.save()





