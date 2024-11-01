# blog/models.py
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        base_slug = slugify(self.title)
        slug = base_slug
        similar_slugs = Post.objects.filter(slug__startswith=base_slug).values_list('slug', flat=True)
        
        if slug not in similar_slugs:
            return slug

        counter = 1
        while slug in similar_slugs:
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def __str__(self):
        return self.title