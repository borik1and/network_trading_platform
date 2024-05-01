# Generated by Django 4.2.7 on 2024-05-01 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0006_factory'),
        ('entrepreneur', '0004_entrepreneur_delete_contacts_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneur',
            name='provider',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='factory.factory', verbose_name='Поставщик'),
        ),
    ]