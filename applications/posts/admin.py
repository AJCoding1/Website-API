from django.contrib import admin

from .models import Post,PostLike,PostView


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','pkid','created_at','status','updated_at']
    list_display_links =  ['title','pkid','created_at','status','updated_at']
    list_filter =  ['title','pkid','created_at','status','updated_at']

admin.site.register(Post,PostAdmin)


# class PostLikeAdmin(admin.ModelAdmin):
#     list_display = ['user.fisrt_name','post.title']
#     list_display_links =  ['user.fisrt_name','post.title']
   
admin.site.register(PostLike)



# class PostViewAdmin(admin.ModelAdmin):
#     list_display = ['user.fisrt_name','post.title', 'ip']
#     list_display_links =  ['user.fisrt_name','post.title','ip']
   

admin.site.register(PostView)

