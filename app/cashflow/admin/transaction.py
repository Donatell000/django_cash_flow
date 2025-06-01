from django import forms
from django.contrib import admin
from django.forms.widgets import Select
from rangefilter.filters import DateRangeFilter

from cashflow.admin.category_by_type_filter import CategoryByTypeFilter
from cashflow.admin.subcategory_by_category_filter import SubcategoryByCategoryAndTypeFilter
from cashflow.models import Transaction, Category, Subcategory


class CategorySelect(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)

        obj = getattr(value, "instance", None)
        if obj and obj.type_id:
            option["attrs"]["data-type-id"] = str(obj.type_id)
        return option


class SubcategorySelect(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex=subindex, attrs=attrs)

        obj = getattr(value, "instance", None)
        if obj and obj.category_id and obj.category and obj.category.type_id:
            option["attrs"]["data-category-id"] = str(obj.category_id)
            option["attrs"]["data-type-id"] = str(obj.category.type_id)
        return option


class TransactionAdminForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
        widgets = {
            "category": CategorySelect,
            "subcategory": SubcategorySelect,
        }

    class Media:
        js = ("transaction_dynamic_filters.js",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()
        self.fields["subcategory"].queryset = Subcategory.objects.select_related("category").all()


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm
    list_display = ("created_at", "amount", "type", "status", "category", "subcategory", "comment",)
    list_filter = (
        ("created_at", DateRangeFilter),
        "type",
        "status",
        CategoryByTypeFilter,
        SubcategoryByCategoryAndTypeFilter,
    )
    search_fields = ("comment",)
    date_hierarchy = "created_at"
