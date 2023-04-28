from django.contrib import admin
from .models import Post, Tag
from django import forms
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from tagify.fields import TagField
# Register your models here.


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    tags = TagField(label='Tags', place_holder='Adicione uma tag', delimiters=',', data_list=[tag.name for tag in Tag.objects.all()])

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            tags=self.instance.tags.all()
            tag_names=','.join([tag.name for tag in tags])
            self.fields['tags'].initial=tag_names

    def save(self, commit=True):
        instance=super(PostForm, self).save(commit=False)
        tags=self.cleaned_data.get('tags', '')
        instance.save()
        instance.tags.clear()
        for tag_name in tags:
            tag, _=Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        if commit:
            instance.save()
        return instance


@ admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display=('title', 'created_at', 'my_tags')
    search_fields=('title', 'content')
    list_filter=('created_at',)
    form=PostForm