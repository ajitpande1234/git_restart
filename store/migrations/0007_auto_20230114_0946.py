# Generated by Django 3.2.16 on 2023-01-14 04:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('Date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
