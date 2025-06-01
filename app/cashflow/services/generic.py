from typing import Any

from django.db.models import Model, QuerySet
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer


class GenericCRUDService:
    def __init__(
        self,
        request: Request,
        model: type[Model],
        serializer_class: type[BaseSerializer],
        pk: int | None = None
    ) -> None:
        self.request: Request = request
        self.model: type[Model] = model
        self.serializer_class: type[BaseSerializer] = serializer_class
        self.pk: int | None = pk

    def get_object(self) -> Model:
        return get_object_or_404(self.model, pk=self.pk)

    def list(self) -> tuple[Any, int]:
        queryset: QuerySet = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return serializer.data, status.HTTP_200_OK

    def create(self) -> tuple[Any, int]:
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.model.objects.create(**serializer.validated_data)
        return self.serializer_class(instance).data, status.HTTP_201_CREATED

    def retrieve(self) -> tuple[Any, int]:
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return serializer.data, status.HTTP_200_OK

    def update(self) -> tuple[Any, int]:
        instance = self.get_object()
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return self.serializer_class(instance).data, status.HTTP_200_OK

    def delete(self) -> tuple[None, int]:
        instance = self.get_object()
        instance.delete()
        return None, status.HTTP_204_NO_CONTENT
