from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .reference import Status, TransactionType, Category, Subcategory


class Transaction(models.Model):
    created_at = models.DateField(
        _("Дата создания"),
        default=timezone.now
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name=_("Статус")
    )
    type = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name=_("Тип")
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name=_("Категория")
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        related_name="transactions",
        verbose_name=_("Подкатегория")
    )
    amount = models.DecimalField(
        _("Сумма"),
        max_digits=12,
        decimal_places=2
    )
    comment = models.TextField(
        _("Комментарий"),
        blank=True, null=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Транзакция")
        verbose_name_plural = _("Транзакции")

    def __str__(self):
        return f"{self.created_at} - {self.amount} ₽"

    def clean(self):
        if self.category.type != self.type:
            raise ValidationError(_("Категория не относится к выбранному типу транзакции."))
        if self.subcategory.category != self.category:
            raise ValidationError(_("Подкатегория не относится к выбранной категории."))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
