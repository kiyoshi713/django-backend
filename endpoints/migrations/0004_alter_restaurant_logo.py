# Generated by Django 4.1.6 on 2023-02-26 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0003_categoriasporrestaurante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.CharField(max_length=100),
        ),
    ]
