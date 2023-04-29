from datetime import date

from django.db import models
from django.utils.html import format_html


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        managed = False
        ordering = ['name']
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name
    
class Influencer(models.Model):
    class Meta:
        verbose_name = "Influencer"
        verbose_name_plural = "Influencers"
        db_table = 'influencers'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    def my_tags(self):
        tags = [tag.name for tag in self.tags.all()]

        html = '<div>'
        for tag in tags:
            html += f'<span class="badge badge-secondary mx-1">{tag}</span>'
        html += '</div>'

        return format_html(html)
    
    tags = models.ManyToManyField(Tag, related_name='influencers', blank=True)
    
    def get_age(self):
        return int((date.today() - self.birth_date).days / 365.25)
    my_tags.short_description = 'Tags'
    my_tags.allow_tags = True