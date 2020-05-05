# Generated by Django 2.2.6 on 2020-05-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200504_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothing',
            name='product',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
