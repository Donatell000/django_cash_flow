from typing import Any

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request

from cashflow.models.reference import Category, Subcategory
from cashflow.models.transaction import Transaction
from cashflow.serializers.transaction import TransactionSerializer


class TransactionService:
    def __init__(self, request: Request, pk: int | None = None) -> None:
        self.request = request
        self.pk = pk

    def get_object(self) -> Transaction:
        return get_object_or_404(Transaction, pk=self.pk)

    def validate_category_and_subcategory(self, data: dict[str, Any]) -> None:
        category: Category = data["category"]
        subcategory: Subcategory = data["subcategory"]
        type_ = data["type"]

        if subcategory.category_id != category.id:
            raise ValidationError("Подкатегория не соответствует выбранной категории.")
        if category.type_id != type_.id:
            raise ValidationError("Категория не соответствует выбранному типу.")

    def handle_get(self) -> tuple[dict[str, Any], int]:
        if self.pk is not None:
            transaction = self.get_object()
            serializer = TransactionSerializer(transaction)
            return serializer.data, status.HTTP_200_OK
        else:
            queryset = Transaction.objects.all()
            serializer = TransactionSerializer(queryset, many=True)
            return serializer.data, status.HTTP_200_OK

    def handle_post(self) -> tuple[dict[str, Any], int]:
        serializer = TransactionSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.validate_category_and_subcategory(serializer.validated_data)
        transaction = Transaction.objects.create(**serializer.validated_data)
        return TransactionSerializer(transaction).data, status.HTTP_201_CREATED

    def handle_put(self) -> tuple[dict[str, Any], int]:
        transaction = self.get_object()
        serializer = TransactionSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.validate_category_and_subcategory(serializer.validated_data)
        for attr, value in serializer.validated_data.items():
            setattr(transaction, attr, value)
        transaction.save()
        return TransactionSerializer(transaction).data, status.HTTP_200_OK

    def handle_delete(self) -> tuple[None, int]:
        transaction = self.get_object()
        transaction.delete()
        return None, status.HTTP_204_NO_CONTENT
