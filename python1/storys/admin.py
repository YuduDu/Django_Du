from django.contrib import admin
from storys.models import Story
# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    fieldsets=[
               (None,{'fields':['title']}),
               ('Content',{'fields':['content']})]
    list_display=('title','content')
    search_fields = ['title']
admin.site.register(Story,StoryAdmin)
