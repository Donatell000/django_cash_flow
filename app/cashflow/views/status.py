from cashflow.models.reference import Status
from cashflow.serializers.reference import StatusSerializer
from cashflow.views.generic import GenericListCreateView, GenericDetailView


class StatusListCreateView(GenericListCreateView):
    model = Status
    serializer_class = StatusSerializer


class StatusDetailView(GenericDetailView):
    model = Status
    serializer_class = StatusSerializer
