from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
    title = models.CharField(
        max_length = 50,
        verbose_name='title'
        )
    parent = TreeForeignKey(
        'self', 
        on_delete = models.CASCADE,
        related_name = 'children', 
        verbose_name = 'parent',
        null = True,
        blank = True
    )
    slug = models.SlugField(
        unique = True,
        verbose_name = 'slug'
        )

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("category_detail", kwargfs = {'slug':self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']
