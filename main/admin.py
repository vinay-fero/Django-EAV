from django.contrib import admin

from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from .models import Order, Organization

admin.site.register([Order])


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    formfield_overrides = {JSONField: {"widget": JSONEditorWidget}}
