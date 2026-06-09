from django.contrib import admin
from . import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "tag_list", "date")
    list_filter = ("author", "tags", "date")
    prepopulated_fields = {
        "slug": ("title",),
    }
    def tag_list(self, obj):
        return ", ".join(tag.caption for tag in obj.tags.all())


admin.site.register(models.Author)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag)
