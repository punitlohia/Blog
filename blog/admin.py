from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Profile,Post,Comment,PostOrignal
from . import createexcelrecord

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class PostInline(admin.StackedInline):
    model = Post
    extra = 3

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,PostInline)

    actions=['createexcelrecord']

    def createexcelrecord(self,request,query):

            createexcelrecord.createrecord(query)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 3

class PostsAdmin(admin.ModelAdmin):
    list_display=('title','description','user','createddatetime')
    inlines=(CommentsInline,)

class PostsOrigrnalAdmin(admin.ModelAdmin):
    list_display=('title','description','user','createddatetime')

class CommentAdmin(admin.ModelAdmin):
    list_display=('comment','post','user','commentdatetime')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Post,PostsAdmin)
admin.site.register(PostOrignal,PostsOrigrnalAdmin)
admin.site.register(Comment,CommentAdmin)
