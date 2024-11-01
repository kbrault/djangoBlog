# your_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('markdownx/', include('markdownx.urls')),  # Include markdownx URLs if using django-markdownx
    path('', include('blog.urls')),  # Include the blog app's URLs
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development (optional)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
