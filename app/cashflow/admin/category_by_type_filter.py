from django.contrib.admin import SimpleListFilter

from cashflow.models import Category


class CategoryByTypeFilter(SimpleListFilter):
    title = "Категория"
    parameter_name = "category"

    def lookups(self, request, model_admin):
        type_id = request.GET.get("type__id__exact")
        qs = Category.objects.all()
        if type_id:
            qs = qs.filter(type_id=type_id)
        return [(c.id, str(c)) for c in qs]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category_id=self.value())
        return queryset
