<<<<<<< HEAD
# Generated by Django 2.2.6 on 2020-05-31 12:05
=======
# Generated by Django 2.2.6 on 2020-06-04 18:18
>>>>>>> 8aa7c4a5ddb21e4d4d4d6f7460f017b70e2da7f0

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_auto_20200526_2334'),
=======
        ('products', '0008_auto_20200526_2334'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> 8aa7c4a5ddb21e4d4d4d6f7460f017b70e2da7f0
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=datetime.datetime.now, null=True)),
<<<<<<< HEAD
                ('address', models.TextField(max_length=1000)),
=======
                ('address', models.TextField(max_length=1000)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('mobile', models.IntegerField()),
>>>>>>> 8aa7c4a5ddb21e4d4d4d6f7460f017b70e2da7f0
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
