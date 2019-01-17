from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile,Post,Comment

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class PostsAdmin(admin.ModelAdmin):
    list_display=('title','description','user','createddatetime')

class CommentAdmin(admin.ModelAdmin):
    list_display=('comment','post','user','commentdatetime')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Post,PostsAdmin)
admin.site.register(Comment,CommentAdmin)
