from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from categories.views import index, category_detail

urlpatterns = [
    path('', index, name = 'homepage'),
    path('cat/<int:id>/', category_detail, name='category_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
