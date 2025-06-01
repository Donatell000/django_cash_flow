from rest_framework.views import APIView
from rest_framework.response import Response

from cashflow.services.generic import GenericCRUDService


class GenericListCreateView(APIView):
    model = None
    serializer_class = None

    def get(self, request):
        service = GenericCRUDService(request, self.model, self.serializer_class)
        data, code = service.list()
        return Response(data, status=code)

    def post(self, request):
        service = GenericCRUDService(request, self.model, self.serializer_class)
        data, code = service.create()
        return Response(data, status=code)


class GenericDetailView(APIView):
    model = None
    serializer_class = None

    def get(self, request, pk):
        service = GenericCRUDService(request, self.model, self.serializer_class, pk=pk)
        data, code = service.retrieve()
        return Response(data, status=code)

    def put(self, request, pk):
        service = GenericCRUDService(request, self.model, self.serializer_class, pk=pk)
        data, code = service.update()
        return Response(data, status=code)

    def delete(self, request, pk):
        service = GenericCRUDService(request, self.model, self.serializer_class, pk=pk)
        data, code = service.delete()
        return Response(data, status=code)
