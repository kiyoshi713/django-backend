# Generated by Django 4.1.6 on 2023-02-23 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='username',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='plato',
            name='restaurante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='endpoints.restaurant'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
