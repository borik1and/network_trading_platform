# Generated by Django 4.2.7 on 2024-05-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0004_remove_factory_contacts_factory_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factory_product',
            old_name='name',
            new_name='name_product',
        ),
        migrations.RemoveField(
            model_name='factory_contacts',
            name='name',
        ),
        migrations.AddField(
            model_name='factory_contacts',
            name='name_contact',
            field=models.CharField(default='', max_length=100, verbose_name='Имя контакта'),
        ),
    ]
