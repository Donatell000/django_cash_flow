from rest_framework import serializers

from cashflow.models.transaction import Transaction
from cashflow.models.reference import Status, TransactionType, Category, Subcategory


class TransactionSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    type = serializers.PrimaryKeyRelatedField(queryset=TransactionType.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subcategory = serializers.PrimaryKeyRelatedField(queryset=Subcategory.objects.all())

    class Meta:
        model = Transaction
        fields = [
            "id",
            "created_at",
            "status",
            "type",
            "category",
            "subcategory",
            "amount",
            "comment",
        ]
