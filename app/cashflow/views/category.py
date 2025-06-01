from cashflow.models.reference import Category
from cashflow.serializers.reference import CategorySerializer
from cashflow.views.generic import GenericListCreateView, GenericDetailView


class CategoryListCreateView(GenericListCreateView):
    model = Category
    serializer_class = CategorySerializer


class CategoryDetailView(GenericDetailView):
    model = Category
    serializer_class = CategorySerializer
