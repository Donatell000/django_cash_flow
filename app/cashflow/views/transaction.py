from rest_framework.response import Response
from rest_framework.views import APIView

from cashflow.services.transaction import TransactionService


class TransactionListCreateView(APIView):
    def get(self, request):
        service = TransactionService(request)
        response_data, status_code = service.handle_get()
        return Response(response_data, status=status_code)

    def post(self, request):
        service = TransactionService(request)
        response_data, status_code = service.handle_post()
        return Response(response_data, status=status_code)


class TransactionDetailView(APIView):
    def get(self, request, pk: int):
        service = TransactionService(request, pk=pk)
        response_data, status_code = service.handle_get()
        return Response(response_data, status=status_code)

    def put(self, request, pk: int):
        service = TransactionService(request, pk=pk)
        response_data, status_code = service.handle_put()
        return Response(response_data, status=status_code)

    def delete(self, request, pk: int):
        service = TransactionService(request, pk=pk)
        response_data, status_code = service.handle_delete()
        return Response(response_data, status=status_code)
