# Generated by Django 4.1.5 on 2023-01-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
