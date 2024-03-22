from django.contrib import admin

# Register your models here.

from .models import Post,Post_By

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('post_name',)}
    list_display=('post_name','title',)


admin.site.register(Post,PostAdmin)
admin.site.register(Post_By)
