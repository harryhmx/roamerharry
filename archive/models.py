from django.db import models
from django.contrib.auth import models as um

class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(um.User, on_delete=models.SET_NULL, related_name='blogs', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    body = models.TextField()
    hits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
