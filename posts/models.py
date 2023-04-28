from django.db import models
from django.utils.html import format_html

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def my_tags(self):
        tags = [tag.name for tag in self.tags.all()]

        html = '<div>'
        for tag in tags:
            html += f'<span class="badge badge-secondary mx-1">{tag}</span>'
        html += '</div>'

        return format_html(html)

    class Meta:
        ordering = ['-created_at']
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
    my_tags.short_description = 'Tags'
    my_tags.allow_tags = True



class Tag(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post, related_name='tags')

    class Meta:
        ordering = ['name']
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
