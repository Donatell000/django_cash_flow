from cashflow.models.reference import TransactionType
from cashflow.serializers.reference import TransactionTypeSerializer
from cashflow.views.generic import GenericListCreateView, GenericDetailView


class TransactionTypeListCreateView(GenericListCreateView):
    model = TransactionType
    serializer_class = TransactionTypeSerializer


class TransactionTypeDetailView(GenericDetailView):
    model = TransactionType
    serializer_class = TransactionTypeSerializer
