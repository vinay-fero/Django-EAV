from django.contrib import admin
from .models import Attribute, AttributeValue


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ("organization", "name", "is_required", "type")
    search_fields = ("organization",)


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ("attribute", "value")
