# Generated by Django 2.2.6 on 2020-06-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentdetails',
            name='trsn_status',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='order_id',
            field=models.CharField(max_length=100, verbose_name='Order Id'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='trsn_amount',
            field=models.CharField(max_length=100, verbose_name='Transaction Amount'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='trsn_date',
            field=models.CharField(max_length=100, verbose_name='Transaction Date'),
        ),
        migrations.AlterField(
            model_name='paymentdetails',
            name='trsn_id',
            field=models.CharField(max_length=100, verbose_name='Transaction id'),
        ),
    ]
