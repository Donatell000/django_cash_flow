from cashflow.models.reference import Subcategory
from cashflow.serializers.reference import SubcategorySerializer
from cashflow.views.generic import GenericListCreateView, GenericDetailView


class SubcategoryListCreateView(GenericListCreateView):
    model = Subcategory
    serializer_class = SubcategorySerializer


class SubcategoryDetailView(GenericDetailView):
    model = Subcategory
    serializer_class = SubcategorySerializer
