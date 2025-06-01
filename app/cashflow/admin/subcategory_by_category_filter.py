from django.contrib.admin import SimpleListFilter

from cashflow.models import Subcategory


class SubcategoryByCategoryAndTypeFilter(SimpleListFilter):
    title = "Подкатегория"
    parameter_name = "subcategory"

    def lookups(self, request, model_admin):
        type_id = request.GET.get("type__id__exact")
        category_id = request.GET.get("category")

        qs = Subcategory.objects.select_related("category")

        if type_id:
            qs = qs.filter(category__type_id=type_id)
        if category_id:
            qs = qs.filter(category_id=category_id)

        return [(s.id, str(s)) for s in qs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subcategory_id=self.value())
        return queryset
