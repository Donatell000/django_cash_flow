# Generated by Django 5.1.4 on 2025-06-01 12:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название типа')),
            ],
            options={
                'verbose_name': 'Тип транзакции',
                'verbose_name_plural': 'Типы транзакций',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='cashflow.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'unique_together': {('name', 'category')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='cashflow.category', verbose_name='Категория')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='cashflow.status', verbose_name='Статус')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='cashflow.subcategory', verbose_name='Подкатегория')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='cashflow.transactiontype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='cashflow.transactiontype', verbose_name='Тип транзакции'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'type')},
        ),
    ]
