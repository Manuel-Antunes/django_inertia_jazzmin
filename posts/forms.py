from django import forms
from tagify.fields import TagField

from .models import Post, Tag


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