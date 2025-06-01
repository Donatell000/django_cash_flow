from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(_("Название статуса"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("Статус")
        verbose_name_plural = _("Статусы")

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(_("Название типа"), max_length=100, unique=True)

    class Meta:
        verbose_name = _("Тип транзакции")
        verbose_name_plural = _("Типы транзакций")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Название категории"), max_length=100)
    type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name=_("Тип транзакции")
    )

    class Meta:
        unique_together = ("name", "type")
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    def __str__(self):
        return f"{self.name} ({self.type.name})"


class Subcategory(models.Model):
    name = models.CharField(_("Название подкатегории"), max_length=100)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name=_("Категория")
    )

    class Meta:
        unique_together = ("name", "category")
        verbose_name = _("Подкатегория")
        verbose_name_plural = _("Подкатегории")

    def __str__(self):
        return f"{self.name} ({self.category.name} — {self.category.type.name})"
