from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from categories.models import Category


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),  
    prepopulated_fields = {'slug':['title']},
)
