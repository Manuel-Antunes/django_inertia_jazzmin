from django.contrib import admin

from .forms import InfluencerAdminForm
from .models import Influencer, Tag


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(Influencer)
class InfluencerAdmin(BaseAdmin):
    list_display=('name', 'birth_date', 'get_age','my_tags')
    search_fields=('name',)
    list_filter=('birth_date',)
    form=InfluencerAdminForm