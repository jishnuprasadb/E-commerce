# Generated by Django 4.1.1 on 2022-10-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0006_rename_product_category_category2_category1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='category1',
        ),
    ]