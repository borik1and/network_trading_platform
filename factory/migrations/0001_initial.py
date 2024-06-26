# Generated by Django 4.2.7 on 2024-04-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory_contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null={'blank': True, 'null': True})),
                ('email', models.EmailField(max_length=254, null={'blank': True, 'null': True})),
                ('country', models.CharField(max_length=100, null={'blank': True, 'null': True})),
                ('city', models.CharField(max_length=100, null={'blank': True, 'null': True})),
                ('street', models.CharField(max_length=100, null={'blank': True, 'null': True})),
            ],
        ),
    ]
