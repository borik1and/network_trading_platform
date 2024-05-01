# Generated by Django 4.2.7 on 2024-05-01 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0005_rename_name_factory_product_name_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contact', models.CharField(default='', max_length=100, verbose_name='Имя контакта')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(default='', max_length=100, verbose_name='Страна')),
                ('city', models.CharField(default='', max_length=100, verbose_name='Город')),
                ('street', models.CharField(default='', max_length=100, verbose_name='Улица')),
                ('house_number', models.CharField(default=0, max_length=100, verbose_name='Номер дома')),
                ('name_product', models.CharField(max_length=100, verbose_name='Имя продукта')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('date_launch', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Задолженность перед поставщиком')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'завод',
                'verbose_name_plural': 'заводы',
            },
        ),
    ]