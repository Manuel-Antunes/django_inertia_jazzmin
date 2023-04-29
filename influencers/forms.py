from django import forms
from tagify.fields import TagField

from .models import Influencer, Tag


class InfluencerAdminForm(forms.ModelForm):
    class Meta:
        model = Influencer
        fields = ['name', 'birth_date']
    tags_field = TagField(label='Tags', place_holder='Adicione uma tag', delimiters=',', data_list=[tag.name for tag in Tag.objects.all()])

    def __init__(self, *args, **kwargs):
        super(InfluencerAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            tags=self.instance.tags.all()
            tag_names=','.join([tag.name for tag in tags])
            self.fields['tags_field'].initial=tag_names

    def save(self, commit=True):
        instance=super(InfluencerAdminForm, self).save(commit=False)
        tags=self.cleaned_data.get('tags_field', '')
        instance.save()
        instance.tags.clear()
        for tag_name in tags:
            tag, _= Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        if commit:
            instance.save()
        return instance