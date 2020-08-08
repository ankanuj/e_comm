from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display=['id','email','created_on']
    list_per_page=25
    list_filter=['email']
    list_display_links=['id','email']

admin.site.register(Feedback,FeedbackAdmin)